clean:
	rm -rf ./*.{*~,s,o,out}
	rm -rf ./usr/lib/*
so: clean obj
	gcc -shared -fPIC -Wl,-soname,libfunc.so.1 -o ./usr/lib/libfunc.so.1.6.0 func.o
	cd ./usr/lib; ln -s libfunc.so.1.6.0 libfunc.so.1; ln -s libfunc.so.1 libfunc.so
obj: 
	g++ -c func.c -o func.o
exe:
	g++ func.o main.c  -o test.out


