# Uncomment song_scm from this line if you have CHICKEN Scheme installed
# http://call-cc.org/
#
# Otherwise, the Scheme example is not built
C = song_cpp song_c
JAVA = song.class
SCHEME = song_scm


# You may also try the clang compiler
CC = gcc
CXX = g++

CXXFLAGS = -std=c++14 -O3 -foptimize-sibling-calls -fno-exceptions -lstdc++
CFLAGS   = -std=c11   -O3

all: $(C) $(JAVA) $(SCHEME)
c: $(C)
java: $(JAVA)
scheme: $(SCHEME)

%.class: %.java
	javac $^

%: %.scm
	csc $(CSCFLAGS) $^

clean:
	-rm -f $(SCHEME) $(C) $(JAVA) *.o core

.PHONY: all c java scheme clean
