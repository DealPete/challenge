x <- read.csv("cipher1.txt", header=FALSE)
y <- as.numeric(x[1,])
za <- c()
zb <- c()
zc <- c()

for (i in seq(1, length(y), by=3))
{
	za <- c(za, y[i])
}

for (i in seq(2, length(y), by=3))
{
	zb <- c(zb, y[i])
}

for (i in seq(3, length(y), by=3))
{
	zc <- c(zc, y[i])
}