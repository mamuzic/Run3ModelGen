# Specify the image from which you are working
FROM gitlab-registry.cern.ch/sft/docker/alma9-core:latest
# FROM gitlab-registry.cern.ch/sft/release/el9:LCG_105
# FROM gitlab-registry.cern.ch/linuxsupport/alma9-base:latest

# Put the current repo (the one in which this Dockerfile resides) in the directory specified here
# Note that this directory is created on the fly and does not need to reside in the repo already
ADD . /workdir

# Go into the directory specified here (again, it will create the directory if it doesn't already exist)
WORKDIR /workdir/

# Create a run directory
# RUN sudo mkdir /Tutorial/run

# Install Run3ModelGen
# RUN source source/setup.sh && \
RUN mkdir build && cd build && \
    cmake ../source && \
    make && \
    ls
    # ls && \
    # source setup.sh

# Add atlas user to root group (needed to avoid permissions issues when writing files on the local machine)
# RUN source ~/release_setup.sh && sudo usermod -aG root atlas