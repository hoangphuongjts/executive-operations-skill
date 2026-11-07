"""Compare submitted PCM16 WAV candidates; never infer perceptual quality from bitrate."""
import argparse,array,hashlib,json,math,sys,wave
from pathlib import Path
WEIGHTS={'accuracy':.35,'naturalness':.25,'identity':.2,'prosody':.15,'cleanliness':.05}
def metrics(path):
 with wave.open(str(path),'rb') as w:
  if w.getsampwidth()!=2 or w.getcomptype()!='NONE':raise ValueError('Cần WAV PCM16; chuyển đổi bản so sánh, giữ nguyên gốc')
  channels,rate,n=w.getnchannels(),w.getframerate(),w.getnframes();a=array.array('h',w.readframes(n))
 if sys.byteorder!='little':a.byteswap()
 if not a:raise ValueError('Âm thanh rỗng')
 rms=math.sqrt(sum((x/32768)**2 for x in a)/len(a));peak=max(abs(x) for x in a)/32768
 return {'duration':n/rate,'sample_rate':rate,'channels':channels,'rms_dbfs':20*math.log10(max(rms,1e-12)),'peak_dbfs':20*math.log10(max(peak,1e-12)),'near_full_scale_fraction':sum(abs(x)>=32760 for x in a)/len(a)}
def evaluate(data,base):
 results=[]
 for c in data['candidates']:
  row={'id':c['id'],'eligible':False,'issues':[]}
  try:
   f=(base/c['file']).resolve();m=metrics(f);row['metrics']=m;row['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
   if not c.get('rights_verified'):row['issues'].append('rights_unverified')
   if c.get('is_clone') and not c.get('speaker_consent'):row['issues'].append('speaker_consent_missing')
   if c.get('script_sha256')!=data.get('script_sha256') or not data.get('script_sha256'):row['issues'].append('script_mismatch_or_unknown')
   if m['near_full_scale_fraction']>.001:row['issues'].append('possible_clipping')
   if m['rms_dbfs']<-55:row['issues'].append('near_silent_review_needed')
   review=c.get('listening_review',{})
   if not review.get('reviewer') or not review.get('full_listen') or review.get('critical_errors')!=False:row['issues'].append('listening_review_missing_or_critical_errors')
   scores=review.get('scores',{})
   if any(isinstance(scores.get(k),bool) or not isinstance(scores.get(k),(int,float)) or not 1<=scores[k]<=5 for k in WEIGHTS):row['issues'].append('scores_missing_or_invalid')
   if not row['issues']:
    row['eligible']=True;row['score']=round(sum(scores[k]*v for k,v in WEIGHTS.items())*20,2)
  except (OSError,ValueError,wave.Error,KeyError) as e:row['issues'].append(str(e))
  results.append(row)
 ranked=sorted([r for r in results if r['eligible']],key=lambda r:r['score'],reverse=True)
 winner=ranked[0]['id'] if ranked and (len(ranked)==1 or ranked[0]['score']-ranked[1]['score']>=2) else None
 return {'results':results,'recommended_candidate':winner,'decision':'human_review_recommendation' if winner else 'abstain_or_tie','note':'Không phải MOS chuẩn hóa; reviewer cung cấp điểm. Không đo SNR, true peak hoặc CER/WER tự động. Ngưỡng kỹ thuật là heuristic.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('--output',required=True);a=p.parse_args();src=Path(a.manifest).resolve();out=Path(a.output)
 if out.exists():raise SystemExit('Không ghi đè báo cáo có sẵn')
 out.write_text(json.dumps(evaluate(json.loads(src.read_text(encoding='utf-8')),src.parent),ensure_ascii=False,indent=2),encoding='utf-8')
