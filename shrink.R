library(readxl)
library(dplyr)
library(plyr)
library(PerformanceAnalytics)
library(car)
library(e1071) #svm
library(Epi) 
library(caret) #cross validation

df <- read_excel("Shrink.xlsx")

df_1 = df[-23,]
df_1 = df_1[-23,]

df_2 <- df_1 %>% filter(Shrinkage_Rate != 'n/a')

df_2$Shrinkage_Rate <- as.numeric(df_2$Shrinkage_Rate)

ggplot(data = df, aes(x=Stress, y = WER)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

cor.test(df_2$Shrinkage_Rate, df_2$Stress)


model_1 <- lm(Stress ~ Shrinkage_Rate, data=df_2)
model_2 <- lm(WER ~ Shrinkage_Rate, data=df_2)
model_3 <- lm(Shrinkage_Rate ~ Stress + WER, data=df_2)

df_3 = df_3[-21,]

df_3$Shrinkage_Rate <- as.numeric(df_3$Shrinkage_Rate)
model_1 <- lm(WER ~ TEOS + HF + LF, data=df_3)
model_2 <- lm(Stress ~ TEOS + HF + LF, data=df_3)
model_3 <- lm(Shrinkage_Rate ~ TEOS + HF + LF, data=df_3)


test <- read_excel("sh.xlsx")
test$Shrink_Target <- as.factor(test$Shrink_Target)

ggplot(data = test, aes(x=Stress, y = WER, color=Shrink_Target)) +
  geom_point(stat = 'identity', cex = 1.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

















