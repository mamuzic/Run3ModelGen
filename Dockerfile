# Specify the image from which you are working
# FROM gitlab-registry.cern.ch/sft/docker/alma9-core:latest
# FROM gitlab-registry.cern.ch/sft/release/el9:LCG_105
FROM gitlab-registry.cern.ch/linuxsupport/alma9-base:latest

# Put the current repo (the one in which this Dockerfile resides) in the directory specified here
# Note that this directory is created on the fly and does not need to reside in the repo already
ADD . /workdir

# Go into the directory specified here (again, it will create the directory if it doesn't already exist)
WORKDIR /workdir/

# Create a run directory
# RUN sudo mkdir /Tutorial/run

# Set default shell to bash:
SHELL ["/bin/bash", "-c"]

# Install Run3ModelGen
# RUN source source/setup.sh && \
RUN curl -fsSL https://pixi.sh/install.sh | bash && \
    . ~/.bash_profile  && \
    # pixi shell -> Is there a way to make this work?
    pwd && \
    ls  && \
    mkdir build; cd build && \
    pixi list && \
    pixi run python --version && \
    pixi run which gcc && \
    pixi run which cc && \
    pixi run which c++ && \
    pixi run cmake ../source && \
    pixi run make && \
    ls && \
    # pixi run source setup.sh && \
    source setup.sh && \
    pixi run genModels.py

CMD ["/bin/bash", "-c", ". ~/.bash_profile && source build/setup.sh && pixi shell"]

# Add atlas user to root group (needed to avoid permissions issues when writing files on the local machine)
# RUN source ~/release_setup.sh && sudo usermod -aG root atlas