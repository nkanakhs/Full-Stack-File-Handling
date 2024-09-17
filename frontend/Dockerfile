# Use the official Node.js image with version 18
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular app
RUN npm run build --prod

# Expose port 4200 for the Angular dev server
EXPOSE 4200 49153

# Start the Angular app
CMD ["ng", "run" , "start" ]
