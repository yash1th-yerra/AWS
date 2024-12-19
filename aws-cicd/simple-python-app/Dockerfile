# base image
FROM python:3.8

#set the working directory

WORKDIR /app


# Copy the requirements file

COPY requirements.txt .

# install the project dependencies

RUN pip install -r requirements.txt

#copy the project code into the container
COPY . .

#Expose the port that flask application will be listening on 

EXPOSE 5000

#Set environment variables if necessary else leave it


#Run the flask application 
CMD [ "python","app.py" ]
