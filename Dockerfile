FROM python
RUN apt-get update && apt-get install python3-pip -y
WORKDIR /alunos_fast_api
COPY alunos_fast_api /alunos_fast_api/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]