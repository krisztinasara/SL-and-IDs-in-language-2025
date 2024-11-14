library(MASS)
library(tidyverse)
library(GGally)
library(lm.beta)

set.seed(5)

# create the variance covariance matrix
sigma = rbind(c(1, -0.8, -0.7), c(-0.8, 1, 0.9), c(-0.7, 0.9, 1))

# create the mean vector
mu = c(10, 5, 2) 

# generate the multivariate normal distribution
df = as.data.frame(mvrnorm(n = 1000, mu = mu, Sigma = sigma))

df = df |>
  mutate(V4 = V2 * 2,
         V5 = V3 * 3)

ggpairs(df)

m1 = lm(V1 ~ V3, df)
summary(m1)
lm.beta(m1)

m2 = lm(V1 ~ V2 + V3, df)
summary(m2)
lm.beta(m2)

m3 = lm(V1 ~ V5, df)
summary(m3)
lm.beta(m3)

m4 = lm(V1 ~ V4 + V5, df)
summary(m4)
lm.beta(m4)
