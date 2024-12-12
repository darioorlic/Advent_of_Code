
# First -------------------------------------------------------------------

Input <- read.table('01_in.txt', sep = ' ')

A <- sort(Input[,1])
B <- sort(Input[,4])

ans <- sum(abs(A-B))

# Second ------------------------------------------------------------------

# A <- c(3,4,2,1,3,3)
# B <- c(4,3,5,3,9,3)

A <- Input[,1]
B <- Input[,4]

ans <- 0
for (i in A) {
  ans <- ans + i * sum(B == i)
}