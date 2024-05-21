# Specify the image from which you are working
FROM gitlab-registry.cern.ch/linuxsupport/alma9-base:latest

# Put the current repo (the one in which this Dockerfile resides) in the directory specified here
# Note that this directory is created on the fly and does not need to reside in the repo already
COPY . /workdir

# Go into the directory specified here (again, it will create the directory if it doesn't already exist)
WORKDIR /workdir/

# Set default shell to bash
SHELL ["/bin/bash", "-c"]

# Install Run3ModelGen
RUN curl -fsSL https://pixi.sh/install.sh | bash && \
    . ~/.bash_profile && \
    pwd && \
    ls  && \
    mkdir run && \
    pixi list && \
    pixi run python --version && \
    pixi run which gcc && \
    pixi run which cc && \
    pixi run which c++ && \
    pixi run build && \
    ls

# Append pixi path and setup script to bashrc
RUN echo "export PATH=$PATH:/root/.pixi/bin" >> ~/.bashrc && \
    source /workdir/build/setup.sh >> ~/.bashrc

# Define commands to be run when entering container
CMD [ "cd run && pixi shell" ]

ENTRYPOINT [ "/bin/bash", "-i", "-c" ]