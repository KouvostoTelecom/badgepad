FROM qmkfm/base_container

ARG WORKDIR=/app
ENV WORKDIR /app
ENV OUTPUTDIR /build
ENV QMK_HOME $WORKDIR/qmk_firmware
VOLUME $OUTPUTDIR
WORKDIR $WORKDIR
RUN git clone -b keyboard/rubberheikki https://github.com/KouvostoTelecom/qmk_firmware.git
RUN git clone https://github.com/dagonis/QuantumDuck.git
RUN qmk setup -y
COPY scripts scripts
COPY src/compile.sh .
COPY src/ducky_convert.py .
CMD ./compile.sh
