FROM python:3.12-slim
ENV PLAYWRIGHT_BROWSERS_PATH=/playwright
WORKDIR /function
COPY requirements.txt /function/requirements.txt
RUN pip install -r requirements.txt && playwright install && playwright install-deps
COPY lambda_function.py /function/lambda_function.py
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "lambda_function.handler" ]

# FROM public.ecr.aws/lambda/python:3.12
# COPY app.py requirements.txt ./
# RUN python3.12 -m pip install -r requirements.txt -t .
# # Command can be overwritten by providing a different command in the template directly.
# CMD ["app.lambda_handler"]
