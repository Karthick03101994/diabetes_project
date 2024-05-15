FROM python:3.11
COPY ./ app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT [ "streamlit","run" ] 
CMD  ["diabetics_predicition.py"]