# pkg

This is a basic package manager that can, at the current moment, install nouns and 
verbs for the user to use.

In order to get all packages in the mirror,

```sh
./pkg list
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