# Use an official OpenJDK runtime as a parent image
FROM amazoncorretto:21-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file into the container at /usr/src/app
COPY untitled.jar /app

# Run the JAR file
ENTRYPOINT ["java", "-jar", "untitled.jar"]
CMD []
