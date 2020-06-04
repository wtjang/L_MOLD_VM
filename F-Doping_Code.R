
library(ggplot2)
library(readxl)
library(dplyr)

df_total <- read.csv("gemini_vhf_2.csv") # 208ea
df_F <- read_xlsx("FSG_191004.xlsx")
df_F$ITEM <- as.factor(df_F$ITEM)


# 1. EDA - Target Variable(Shrinkage Rate, Stress, R.I)

# 1.1 Shrinkage Rate & Stress

f_data <- df_total %>% filter(Doping == 'F')
f_lm <- lm(STR ~ SHRINK, data = f_data)
cor.test(f_data$STR, f_data$SHRINK) # 0.60
cor.test(f_data$STR, f_data$SHRINK) # 0.60
cor.test(f_data$STR, f_data$SHRINK) # 0.60


fno_data <- df_total %>% filter(Doping == 'NO')
fno_lm <- lm(STR ~ SHRINK, data = fno_data)
cor.test(fno_data$STR, fno_data$SHRINK) # 0.72
cor.test(fno_data$STR, fno_data$SHRINK) # 0.72
cor.test(fno_data$STR, fno_data$SHRINK) # 0.72


# All area
ggplot(data = df_total, aes(x=SHRINK, y = STR, color = Doping)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  stat_smooth(method=lm) +
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-250,-150,-50, 50, 150, 250, 350)) +
  annotate("text", x=4, y=-50, label=expression(italic("y = 42x -124, cor = 60%")), color = "indianred3") +
  annotate("text", x=4.5, y=150, label=expression(italic( "y = 109x - 237, cor = 72%")), color = "deepskyblue3") 


# R.I & Stress
ggplot(data = df_total, aes(x=RI, y = STR, color = Doping)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("R.I") + ylab("STRESS") + 
  stat_smooth(method=lm) +
  scale_y_continuous(breaks = c(-400,-300,-200,-100,0, 100))
  
# R.I & Shrink
ggplot(data = df_total, aes(x=RI, y = SHRINK, color = Doping)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("R.I") + ylab("Shrinkage Rate") + 
  stat_smooth(method=lm)  + 
  scale_y_continuous(breaks = c(-2,-1,0,1,2,3,4))
  
# Si-F/-Si-O & Shrink
ggplot(data = df_F, aes(x=df_F$`Si-F/Si-O` , y = Shrinkage)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Si-F/Si-O") + ylab("Shrinkage Rate") + 
  stat_smooth(method=lm)  + 
  scale_y_continuous(breaks = c(-2,-1,0,1,2,3,4)) + 
  scale_x_continuous(breaks = c(0,1,2,3,4,5,6))

# Si-F/-Si-O & Stress
ggplot(data = df_F, aes(x=df_F$`Si-F/Si-O` , y = STR)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Si-F/Si-O") + ylab("Stress") + 
  stat_smooth(method=lm) +
  scale_x_continuous(breaks = c(0,1,2,3,4,5,6)) + 
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50))
  
# Si-F/-Si-O & R.I
ggplot(data = df_F, aes(x=df_F$`Si-F/Si-O` , y = RI)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Si-F/Si-O") + ylab("R.I") + 
  stat_smooth(method=lm) +
  scale_y_continuous(breaks = c(1.40,1.41,1.42,1.43,1.44,1.45,1.46,1.47))+
  scale_x_continuous(breaks = c(0,1,2,3,4,5,6))

lm_model_R_I_SI_F = lm(df_F$RI ~ df_F$`Si-F/Si-O`, data = df_F)
summary(lm_model_R_I_SI_F)

# Shrinkage & Stress
ggplot(data = df_F, aes(x=Shrinkage , y =STR, color = ITEM)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("Stress") +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50)) + 
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4))
  
# cor plot
library(corrplot)
library(PerformanceAnalytics)

target_var <- df_F[,c(8:14)]

target_var_cor <- cor(target_var, use = "pairwise.complete.obs" )
corrplot.mixed(target_var_cor, tl.col="black", tl.pos = "lt")

chart.Correlation(target_var, histogram=TRUE, pch="+")

chart.Correlation(df_F_data, histogram=TRUE, pch="+")

df_F_data_cor <- cor(df_F_data, use = "pairwise.complete.obs" )
corrplot.mixed(df_F_data_cor, tl.col="black", tl.pos = "lt")

# mol

# median

df_mol <- read.csv("gemini_vhf_6.csv") 

ggplot(data = df_mol, aes(x=Shrinkage, y = STR, color = mol)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  stat_smooth(method=lm) +
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50,100))

df_mol_L <- df_mol %>% filter(mol == 'L')
df_mol_H <- df_mol %>% filter(mol == 'H')

df_mol_L_lm <- lm(STR ~ Shrinkage, data = df_mol_L)
df_mol_H_lm <- lm(STR ~ Shrinkage, data = df_mol_H)

summary(df_mol_L_lm)
summary(df_mol_H_lm)

cor.test(df_mol_L$Shrinkage, df_mol_L$STR)
cor.test(df_mol_H$Shrinkage, df_mol_H$STR)

df_mol_H_lm_pol <- lm(STR ~ Shrinkage + I(Shrinkage^2), data = df_mol_H)
df_mol_L_lm_pol <- lm(STR ~ Shrinkage + I(Shrinkage^2), data = df_mol_L)

summary(df_mol_H_lm_pol)
summary(df_mol_L_lm_pol)

ggplot(data = df_mol, aes(x=Shrinkage, y = STR, color = mol)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50,100)) +
  stat_smooth(data = df_mol_L, method = "lm", formula =y ~ poly(x,2)) +
  stat_smooth(data = df_mol_H, method = "lm")
  

ggplot(data = df_mol, aes(x=Shrinkage, y = STR)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50,100)) +
  stat_smooth(method = "lm", formula =y ~ poly(x,2))
  

# High, Low : 1.8

df_mol_2 <- read.csv("gemini_vhf_7.csv")

ggplot(data = df_mol_2, aes(x=Shrinkage, y = STR, color = mol)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  stat_smooth(method=lm) +
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50,100))

df_mol_L_2 <- df_mol_2 %>% filter(mol == 'L')
df_mol_H_2 <- df_mol_2 %>% filter(mol == 'H')

df_mol_L_2_lm <- lm(STR ~ Shrinkage, data = df_mol_L_2)
df_mol_H_2_lm <- lm(STR ~ Shrinkage, data = df_mol_H_2)

summary(df_mol_L_2_lm)
summary(df_mol_H_2_lm)

df_mol_L_2_lm_pol <- lm(STR ~ Shrinkage + I(Shrinkage^2), data = df_mol_L_2)

ggplot(data = df_mol_2, aes(x=Shrinkage, y = STR, color = mol)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  scale_x_continuous(breaks = c(-2,-1,0,1,2,3,4)) +
  scale_y_continuous(breaks = c(-350,-300,-250,-200,-150,-100,-50,0,50,100)) +
  stat_smooth(data = df_mol_L_2, method = "lm", formula =y ~ poly(x,2)) +
  stat_smooth(data = df_mol_H_2, method = "lm")

cor.test(df_mol_H_2$Shrinkage, df_mol_H_2$STR)
cor.test(df_mol_L_2$Shrinkage, df_mol_L_2$STR)

# Model - RandomForest
# df_total <- read.csv("gemini_vhf_2.csv") #raw data 213

df_total <- read.csv("gemini_vhf_8.csv")
df_total$FREQ <- as.factor(df_total$FREQ)

# doping data -> make model 38ea

# df_F_data <- df_total %>% filter(Doping == 'F')
#df_F_data <- df_F_data[,c("TEOS", "O2", "TEMP", "SIF4", "N2O_Post", "SHRINK","STR")]
#df_F_data <- df_F_data[c(1:31, 35,36,37,38),] #remove N2O


library(caret)
library(randomForest)

train_idx <- sample(1:nrow(df_total), size = 0.8*nrow(df_total), replace = F)
train <- df_total[train_idx,] #3000, 5000
test <-  df_total[-train_idx,]

# Randomforest
SHRINK_rf = randomForest(SHRINK ~ TEOS + O2 + TEMP + SIF4 + HF + LF, data=train, ntree = 4000, mtry = floor(sqrt(2)))
STR_rf = randomForest(STR ~ TEOS + O2 + TEMP+ SIF4 + HF + LF, data=train, ntree = 4000, mtry = floor(sqrt(2)))

SHRINK_test_rf = predict(SHRINK_rf, newdata = test)
STR_test_rf = predict(STR_rf, newdata = test)

plot(test$SHRINK, SHRINK_test_rf)
cor.test(test$SHRINK, SHRINK_test_rf)
plot(test$STR, STR_test_rf)
cor.test(test$STR, STR_test_rf)

# Regression

SHRINK_lm = lm(SHRINK ~ TEOS + O2 + TEMP + SIF4 + HF + LF, data=train)
STR_lm = lm(STR ~ TEOS + O2 + TEMP+ SIF4 + HF + LF, data=train)

SHRINK_test_lm = predict(SHRINK_lm, newdata = test)
STR_test_lm = predict(STR_lm, newdata = test)

plot(test$SHRINK, SHRINK_test_lm)

cor.test(test$SHRINK, SHRINK_test_lm)
plot(test$STR, STR_test_lm)
cor.test(test$STR, STR_test_lm)


sample <- read_xlsx("rf_sample.xlsx")



rf_SHRINK_sample_df = predict(SHRINK_rf, newdata = sample)
lm_STR_sample_df = predict(STR_lm, newdata = sample)




df_sample <- cbind(rf_SHRINK_sample_df, lm_STR_sample_df)
df_sample <- data.frame(df_sample)


write.table(df_sample, "C:/Users/wtjang/Documents/work/20200115_LowShrinkage.csv", 
            sep = ",", row.names = FALSE, quote = FALSE, append = TRUE,  na = "NA")


plot(df_sample$rf_SHRINK_sample_df, df_sample$lm_STR_sample_df)


ggplot(data = df_sample, aes(x=rf_SHRINK_sample_df, y = lm_STR_sample_df)) +
  geom_point(stat = 'identity', cex = 1) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Shrinkage Rate") + ylab("STRESS") + 
  scale_x_continuous(breaks = c(0,0.4,1,2,3)) +
  scale_y_continuous(breaks = c(-500,-400,-300,-200,-100,-50,0,50,100,200,300,400,500))
  








test_1 <- df_sample %>% filter((rf_SHRINK_sample_df<0.6)&(rf_SHRINK_sample_df>0.4))

test_2 <- test_1 %>% filter((test_1$lm_STR_sample_df<-300))

test_2 <- df_sample %>% filter((rf_SHRINK_sample_df<0.6)&(rf_SHRINK_sample_df>0.4)&(lm_STR_sample_df<-100)&(lm_STR_sample_df>-150))






# Model - RandomForest
# df_total <- read.csv("gemini_vhf_2.csv") #raw data 213

sample_test <- read.csv("gemini_vhf_9.csv")
sample_test$Section <- as.factor(sample_test$Section)


ggplot(data = sample_test, aes(x=HF, y = LF, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("HF") + ylab("LF")

ggplot(data = sample_test, aes(x=TEOS, y = TEMP, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("TEOS") + ylab("TEMP")

ggplot(data = sample_test, aes(x=TEOS, y = O2, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("TEOS") + ylab("O2")

ggplot(data = sample_test, aes(x=TEMP, y = O2, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("TEMP") + ylab("O2")

ggplot(data = sample_test, aes(x=TEOS, y = LF, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("TEOS") + ylab("LF")

ggplot(data = sample_test, aes(x=TEOS, y = HF, color = Section)) +
  geom_point(stat = 'identity', cex = 2) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("TEOS") + ylab("HF")



