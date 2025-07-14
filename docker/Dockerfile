FROM ros:humble

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    nano \
    ros-humble-rviz2 \
    ros-humble-rqt-common-plugins \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

COPY ./ros_packages/ /ros2_ws/src/

# Build the workspace
RUN . /opt/ros/humble/setup.sh && \
    colcon build --symlink-install

RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc && \
    echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
    
CMD ["/bin/bash"] 
