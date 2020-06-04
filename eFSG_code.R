library(ggplot2)
library(readxl)
library(dplyr)

df <- read_xlsx("Void_Free_Data.xlsx")

df$SiF4_Exist <- as.factor(df$SiF4_Exist)
df$DOE <- as.factor(df$DOE)
df$Window <- as.factor(df$Window)

#1 EDA
#1.1 Y ~ SiF4 Free 
ggplot(data = df, aes(x=Void_Bottom_up, y = Stress, color = SiF4_Exist)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("Stress") +
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))

ggplot(data = df, aes(x=Void_Bottom_up, y = WER, color = SiF4_Exist)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Void_Bottom_up") + ylab("WER") +
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))

ggplot(data = df, aes(x=Stress, y = WER, color = SiF4_Exist)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))

cor.test(df$Void_Bottom_up, df$WER)
cor.test(df$Void_Bottom_up, df$Stress)
cor.test(df$Stress, df$WER)

#1.2 Y ~ DOE

ggplot(data = df, aes(x=Void_Bottom_up, y = Stress, color = DOE)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("Stress") +
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))

ggplot(data = df, aes(x=Void_Bottom_up, y = WER, color = DOE)) +
  geom_point(stat = 'identity', cex = 3.5) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Void_Bottom_up") + ylab("WER") +
  theme(legend.text = element_text(size = 13)) +
  theme(legend.title = element_text(size = 13)) + 
  theme(axis.title = element_text(size = 14)) + 
  stat_smooth(method = "lm")

ggplot(data = df, aes(x=Stress, y = WER, color = DOE)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))

# DOE1 Check, x <- df[df$DOE == 'DOE1',]
# ggplot(data = x, aes(x=Void_Bottom_up, y = Stress)) +
#   geom_point(stat = 'identity', cex = 3) +
#   theme(panel.grid.major = element_line(color = "grey80" )) +
#   theme(axis.text = element_text(size = rel(1.5))) +
#   xlab("Void_Bottom_up") + ylab("Stress") +
#   theme(legend.text = element_text(size = 14)) +
#   theme(legend.title = element_text(size = 14)) + 
#   theme(axis.title = element_text(size = 15))

df_1 <- df[df$Fluorine_Conc >0,]

ggplot(data = df_1, aes(x=Fluorine_Conc, y = Void_Bottom_up)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Fluorine_Conc") + ylab("Void_Bottom_up") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$Fluorine_Conc, df_1$Void_Bottom_up)

ggplot(data = df_1, aes(x=Fluorine_Conc, y = WER)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Fluorine_Conc") + ylab("WER") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$Fluorine_Conc, df_1$WER)

ggplot(data = df_1, aes(x=Fluorine_Conc, y = Stress)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Fluorine_Conc") + ylab("Stress") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$Fluorine_Conc, df_1$Stress)

ggplot(data = df_1, aes(x=Fluorine_Conc, y = Void_Area)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Fluorine_Conc") + ylab("Void_Area") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$Fluorine_Conc, df_1$Void_Area)

ggplot(data = df_1, aes(x=TEOS, y = Fluorine_Conc)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("TEOS") + ylab("Fluorine_Conc") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$TEOS, df_1$Fluorine_Conc)

ggplot(data = df_1, aes(x=SiF4, y = Fluorine_Conc)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4") + ylab("Fluorine_Conc") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test(df_1$SiF4, df_1$Fluorine_Conc)

ggplot(data = df_1, aes(x=SiF4/TEOS, y = Fluorine_Conc)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4/TEOS") + ylab("Fluorine_Conc") + 
  theme(axis.title = element_text(size = 15))+ 
  stat_smooth(method = "lm")

cor.test((df_1$SiF4/df_1$TEOS), df_1$Fluorine_Conc)

ggplot(data = df_1, aes(x=TEOS, y = WER)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("TEOS") + ylab("WER") + 
  stat_smooth(method = "lm") +
  theme(axis.title = element_text(size = 15))

ggplot(data = df_1, aes(x=TEOS, y = WER)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("TEOS") + ylab("WER") + 
  stat_smooth(method = "lm", formula = y ~ x + I(x^2)) +
  theme(axis.title = element_text(size = 15))

ggplot(data = df_1, aes(x=TEOS, y = Void_Bottom_up)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("TEOS") + ylab("Void_Bottom_up") + 
  theme(axis.title = element_text(size = 15))


ggplot(data = df_1, aes(x=Pressure, y = Fluorine_Conc)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("TEOS") + ylab("Void_Bottom_up") + 
  theme(axis.title = element_text(size = 15))

#3. eFSG
df_3 <- df[df$DOE == 'eFSG Window',]

ggplot(data = df_3, aes(x=Void_Bottom_up, y = Stress, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("Stress") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) +
  geom_text(aes(label=Window, vjust=-1, hjust=0), size=6)

ggplot(data = df_3, aes(x=Void_Bottom_up, y = WER, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))+
  geom_text(aes(label=Window, vjust=-1, hjust=0),size=6)

ggplot(data = df_3, aes(x=Stress, y = WER, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))+
  geom_text(aes(label=Window,  vjust=-1, hjust=0),size=6)+
  stat_smooth(method = "lm")
  
ggplot(data = df_4, aes(x=Void_Bottom_up, y = Stress, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("Stress") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) +
  geom_text(aes(label=Window,  vjust=-1, hjust=0),size=6)

ggplot(data = df_4, aes(x=Void_Bottom_up, y = WER, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Void_Bottom_up") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))+
  geom_text(aes(label=Window,  vjust=-1, hjust=0),size=6)


ggplot(data = df_4, aes(x=Stress, y = WER, color = Window)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("Stress") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 16))+
  geom_text(aes(label=Window,  vjust=-1, hjust=0),size=6)

#5. D/R에 따른 특성치 변화

ggplot(data = df, aes(x=D_R, y = Void_Bottom_up)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("D_R") + ylab("Void_Bottom_up") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 16)) + 
  stat_smooth(method = "lm")

cor.test(df$D_R, df$Void_Bottom_up)  # 0.44
lm_Void_Bottom_up = lm(Void_Bottom_up ~ D_R , data=df)

ggplot(data = df, aes(x=D_R, y = Stress)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("D_R") + ylab("Stress") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 16)) + 
  stat_smooth(method = "lm")

cor.test(df$D_R, df$Stress)  # 0.51
lm_Stress = lm(Stress ~ D_R , data=df)

ggplot(data = df, aes(x=D_R, y = WER)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("D_R") + ylab("WER") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 16)) + 
  stat_smooth(method = "lm")

cor.test(df$D_R, df$WER)  # 0.43
lm_WER = lm(WER ~ D_R , data=df)


ggplot(data = df, aes(x=D_R, y = Void_Area)) +
  geom_point(stat = 'identity', cex = 4) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("D_R") + ylab("Void_Area") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 16)) + 
  stat_smooth(method = "lm")

cor.test(df$D_R, df$Unif)  # 0.43
cor.test(df$D_R, df$R_I)  # 0.43
cor.test(df$D_R, df$Void_Area)  # 0.43

lm_Unif = lm(Unif ~ D_R , data=df)


ggplot(data = df, aes(x=SiF4/TEOS, y = Void_Bottom_up)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4/TEOS") + ylab("Void_Bottom_up") + 
  stat_smooth(method = "lm") +
  theme(axis.title = element_text(size = 15))



ggplot(data = df, aes(x=SiF4/TEOS, y = Void_Area)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4/TEOS") + ylab("Void_Area") + 
  stat_smooth(method = "lm") +
  theme(axis.title = element_text(size = 15))

ggplot(data = df, aes(x=SiF4/TEOS, y = Stress)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4/TEOS") + ylab("Stress") + 
  stat_smooth(method = "lm") +
  theme(axis.title = element_text(size = 15))

ggplot(data = df, aes(x=SiF4/TEOS, y = WER)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(2))) +
  xlab("SiF4/TEOS") + ylab("WER") + 
  stat_smooth(method = "lm") +
  theme(axis.title = element_text(size = 15))


cor.test(df$SiF4/df$TEOS, df$Void_Bottom_up)
cor.test(df$SiF4/df$TEOS, df$Void_Area)
cor.test(df$SiF4/df$TEOS, df$Stress)
cor.test(df$SiF4/df$TEOS, df$WER)

# ML

library(caret)
library(randomForest)

df_final = na.omit(df)

train_idx <- sample(1:nrow(df_final), size = 0.8*nrow(df_final), replace = F)
train <- df_final[train_idx,] #3000, 5000
test <-  df_final[-train_idx,]

# Randomforest
Void_rf = randomForest(Void_Bottom_up ~ SiF4 + TEOS + Pressure + HF + LF, data=train, ntree = 500, mtry = 2)
WER_rf = randomForest(WER ~ SiF4 + TEOS + Pressure + HF + LF, data=train, ntree = 500, mtry = 2)
Stress_rf = randomForest(Stress ~ SiF4 + TEOS + Pressure + HF + LF, data=train, ntree = 500, mtry = 2)

Void_test_rf = predict(Void_rf, newdata = test)
WER_test_rf = predict(WER_rf, newdata = test)
Stress_test_rf = predict(Stress_rf, newdata = test)

plot(test$Void_Bottom_up, Void_test_rf)
cor.test(test$Void_Bottom_up, Void_test_rf)
plot(test$WER, WER_test_rf)
cor.test(test$WER, WER_test_rf)
plot(test$Stress, Stress_test_rf)
cor.test(test$Stress, Stress_test_rf)

# Linear Regression
Void_lm = lm(Void_Bottom_up ~ SiF4 + TEOS + Pressure + HF + LF, data=train)
WER_lm = lm(WER ~ SiF4 + TEOS + Pressure + HF + LF, data=train)
Stress_lm = lm(Stress ~ SiF4 + TEOS + Pressure + HF + LF, data=train)

Void_test_lm = predict(Void_lm, newdata = test)
WER_test_lm = predict(WER_lm, newdata = test)
Stress_test_lm = predict(Stress_lm, newdata = test)

# eval
plot(test$Void_Bottom_up, type='o',lwd = 2)
lines(Void_test_rf, type='o', col='red',lwd = 2)
lines(Void_test_lm, type='o', col='blue',lwd = 2)
legend(2,0.8,c("Observation","RandomForest model","Linear regression model"),lwd=2,col=c("black","red","blue"))

plot(test$WER, type='o', ylim=c(75, 165),lwd = 2)
lines(WER_test_rf, type='o', col='red',lwd = 2)
lines(WER_test_lm, type='o', col='blue',lwd = 2)
legend(4,160,c("Observation","RandomForest model","Linear regression model"),lwd=2,col=c("black","red","blue"))

plot(test$Stress, type='o',lwd = 2)
lines(Stress_test_rf, type='o', col='red',lwd = 2)
lines(Stress_test_lm, type='o', col='blue',lwd = 2)
legend(5,-20,c("Observation","RandomForest model","Linear regression model"),lwd=2,col=c("black","red","blue"))


vm_test <- read_xlsx("Void_test.xlsx")

Void_test_vm = predict(Void_lm, newdata = vm_test)
WER_test_vm = predict(WER_lm, newdata = vm_test)
Stress_test_vm = predict(Stress_lm, newdata = vm_test)











