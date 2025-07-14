FROM ros:humble

RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    nano \
    libgpiod2 \
    python3-lgpio \
    python3-libgpiod \
    build-essential \
    python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/joan2937/pigpio.git /opt/pigpio && \
    cd /opt/pigpio && \
    make && make install

RUN python3 -m pip install pigpio gpiozero

WORKDIR /ros2_ws
COPY ./src/ ./src/
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build --symlink-install"

RUN echo 'source /opt/ros/humble/setup.bash' >> /root/.bashrc && \
    echo 'source /ros2_ws/install/setup.bash' >> /root/.bashrc

CMD ["/bin/bash"]
