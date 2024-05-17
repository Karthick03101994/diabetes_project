FROM python:3.11
COPY ./ app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENV STREAMLIT_SERVER_PORT 8501
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0
ENTRYPOINT [ "streamlit","run" ] 
CMD  ["diabetics_predicition.py"]
