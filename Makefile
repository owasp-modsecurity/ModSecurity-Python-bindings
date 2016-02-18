all:
	swig -I/usr/local/modsecurity/include/ -python -builtin -Wall -Wextra -c++ modsecurity/modsecurity.i
	python setup.py build_ext --inplace

test:
	tests/t.py

install: all test
	python setup.py install --prefix=/usr

clean:
	rm -f ./modsecurity/modsecurity_wrap.cxx
	rm -rf ./build
	rm -f ./_modsecurity.so
	rm -f ./modsecurity/modsecurity.py
	rm -f ./*.pyc ./tests/*.pyc ./modsecurity/*.pyc



