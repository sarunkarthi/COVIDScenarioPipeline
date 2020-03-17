You need all of your developer tools for R plus:

```
brew install pkg-config
brew install udunits
brew install freestyle
brew install cairo
brew install gdal
```

to get all of the R packages to load. Note that even with this
I couldn't get the `sf` package to install correctly b/c of a
weird proj pkg-config issue that I'm going to have to try to
sort out a little later.
