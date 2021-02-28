FROM continuumio/anaconda3:4.4.0
COPY . /usr/app
EXPOSE 5000
WORKDIR /usr/app
RUN pip install --upgrade pip
RUN rm -rf /opt/conda/lib/python3.6/site-packages/numpy 
RUN pip install -r requirement.txt --ignore-installed
#RUN conda update --all
CMD python app.py
