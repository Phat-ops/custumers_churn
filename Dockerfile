FROM python:3.13
LABEL tac_gia="phat06"

WORKDIR /phat06

COPY model.pkl /phat06/model.pkl
COPY fast.py /phat06/fast.py
COPY requirements.txt /phat06/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["uvicorn", "fast:app","--host","0.0.0.0","--port","8888" ]