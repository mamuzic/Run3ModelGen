# please put here your preferred F95/F2003 compiler
# the options in src/Makefile have been put for the
# cases NAG's nagfor, gfortran, g95, Lahey's lf95 and Intels ifort
# Please uncomment the corresponding line
# F90 = nagfor
F90 = gfortran
# F90 = g95
# F90 = lf95
# F90 = ifort
Model = src
version = 400.00
BUILD_DIR = $(abspath ${CMAKE_BINARY_DIR})
bin/SPheno:
	mkdir -p ${BUILD_DIR}/bin ${BUILD_DIR}/lib ${BUILD_DIR}/include
	cd ${Model} ; ${MAKE} F90=${F90} version=${version}
clean:
	rm -f *.o *~ */*.o */*~
cleanall:
	rm -f bin/SPheno lib/*.a *.o *~ */*.o */*~ include/*
.PHONY: bin/SPheno clean cleanall
