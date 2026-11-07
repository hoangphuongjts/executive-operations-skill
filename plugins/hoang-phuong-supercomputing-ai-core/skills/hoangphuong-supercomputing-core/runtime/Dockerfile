FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY platform128.py profiles.json registry.json evals_128.jsonl seed_knowledge.py cluster_debate.py dashboard.html /app/
RUN useradd -r -u 10001 agent && mkdir -p /data && chown 10001:10001 /data
USER 10001
EXPOSE 8765
CMD ["python", "platform128.py", "serve", "--host", "0.0.0.0", "--port", "8765"]
