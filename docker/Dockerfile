FROM ros:humble

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    nano \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install gpiozero

WORKDIR /ros2_ws

COPY ./src/ /ros2_ws/src/

# Build the workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc && \
    echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
    
CMD ["/bin/bash"] 
