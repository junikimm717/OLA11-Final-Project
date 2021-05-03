# pkg

This is a basic package manager that can, at the current moment, install nouns and 
verbs for the user to use.

In order to search for locally installed packages,

```sh
./pkg list (pattern or none to display everything)
```

In order to search for packages on the mirror,

```sh
./pkg search (pattern or none to display everything)
```

In order to install,
```
./pkg install (package)
```

In order to uninstall,

```sh
./pkg remove (package)
```

Note that pkg will automatically generate a pkg.lock file in its directory, which you should **not** try to remove (it lists the packages currently installed).
