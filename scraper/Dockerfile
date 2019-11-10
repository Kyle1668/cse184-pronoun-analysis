FROM joyzoursky/python-chromedriver:3.6-alpine3.7-selenium

WORKDIR /usr/src/pronouns_analysis
COPY . /usr/src/pronouns_analysis

ENV PATH="${PATH};/usr/src/pronouns_analysis/drivers"

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip3 install requests \
                 beautifulsoup4 \
                 selenium \
                 webdriver-manager \
                 python-dotenv

CMD ["python3", "linkedin_scraper.py"]