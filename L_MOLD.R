library(readxl)
library(dplyr)
library(plyr)
library(PerformanceAnalytics)
library(car)
library(e1071) #svm
library(Epi) 
library(caret) #cross validation

df <- read_excel("train.xlsx")

#1. Change data type

colnames(df) #변수명 확인 후 몇개 골라주기
df <- rename(df, c("D/R" = "D_R", "Pres." = "Pres", "R.I" = "R_I", "Unif." = "Unif", "stress" = "stress")) 
factor_name = c("Temp", "N2", "NH3", "SiH4", "Pres", "HF", "LF", "Gap", "D_R","R_I", "stress", "Unif")

test <- df %>% select(factor_name) 

test <- na.omit(test)
test$Temp <- as.numeric(test$Temp)
test$N2 <- as.numeric(test$N2)
test$NH3 <- as.numeric(test$NH3)
test$SiH4 <- as.numeric(test$SiH4)
#test$Ar <- as.numeric(test$Ar)
test$Pres <- as.numeric(test$Pres)
test$HF <- as.numeric(test$HF)
test$LF <- as.numeric(test$LF)
test$Gap <- as.numeric(test$Gap)
test$D_R <- as.numeric(test$D_R)
test$R_I <- as.numeric(test$R_I)
test$Unif <- as.numeric(test$Unif)
test$stress <- as.numeric(test$stress)
test <- na.omit(test) ## Example : 1420 


summary(test) # 

plot(test$D_R)
test <- subset(test, test$D_R < 4000) #outlier
test <- subset(test, test$D_R > 1000) #outlier

plot(test$R_I)
test <- subset(test, test$R_I < 2) #outlier

#test <- subset(test, test$Temp >= 540)
#test <- subset(test, test$Pres >= 3.0)

plot(test$stress)
test <- subset(test, test$stress >= 0)
#test <- subset(test, test$stress <= 700)

library(ggplot2)
# ggplot(data = test) +
#   geom_bin2d(mapping = aes(x = test$D_R, y = test$R_I))

ggplot(data = test) + geom_point(mapping = aes(x = test$R_I, y = test$D_R))

# Data -> 944obbs

# 2. D/R

#2.1 raw value
train_idx <- sample(1:nrow(test), size = 0.8 * nrow(test), replace = FALSE)
train_mold <- test[train_idx, ]
test_mold <- test[-train_idx, ]

#2.1.1 reg
reg_model_D_R <- lm(D_R ~ N2 + NH3 + SiH4 + Pres + HF + Gap, data=train_mold)
summary(reg_model_D_R)


pred_D_R_reg <- predict(reg_model_D_R, test_mold, interval = "confidence")
test_mold$pred_D_R_reg <- pred_D_R_reg

plot(test_mold$D_R, type = "l",lty=1, lwd=2)
lines(test_mold$pred_D_R_reg[,1], type="l", col = "red",lty=1, lwd=2)
legend(x=40, y=1200, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)

reg_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$D_R - test_mold$pred_D_R_reg[,1])/test_mold$D_R))


#2.1.2 svm

#reg_model_svm <- svm(D_R ~ Temp + N2 + NH3 + SiH4 + Ar + Pres + HF + LF + Gap, data=train_mold)#, gamma=1, cost=16)
#gamma = 1, cost=16, MSE Increase..
#model_svm <- svm(D_R ~ Temp + N2 + NH3 + SiH4 + HF, data=train_mold)
model_svm <- svm(D_R ~ N2 + NH3 + SiH4 + Pres + HF + Gap, data=train_mold)
summary(model_svm)

pred_D_R_svm <- predict(model_svm, test_mold, interval = "confidence")
test_mold$pred_D_R_svm <- pred_D_R_svm

plot(test_mold$D_R, type = "l",lty=1, lwd=2)
lines(test_mold$pred_D_R_svm, type="l", col = "blue",lty=1, lwd=2)
legend(x=40, y=1200, c("D_R","Predict"), col = c("black", "blue"), lty = 1, lwd=3, cex=1)

svm_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$D_R - test_mold$pred_D_R_svm)/test_mold$D_R))
svm_MAPE
##################################################################################################

# 1) only input scale
# 2) input and output scale

#2.2 sacle value
temp <- scale(test,)
#test_scale <- cbind(temp,test$D_R,test$R_I,test$stress)
test_scale <- as.data.frame(temp)
#test_scale <- rename(test_scale, c("V10" = "D_R", "V11" = "R_I", "V12" = "stress"))

train_mold_scale <- test_scale[train_idx, ]
test_mold_scale <- test_scale[-train_idx, ]

#2.2.1 reg  -----------------> same result....with no scale
reg_model_D_R_scale <- lm(D_R ~ Temp + N2 + NH3 + SiH4 + Ar + Pres + HF + LF + Gap, data=train_mold_scale)
summary(reg_model_D_R_scale)

pred_D_R_reg_scale <- predict(reg_model_D_R_scale, test_mold_scale, interval = "confidence")
test_mold_scale$pred_D_R_reg_scale <- pred_D_R_reg_scale


plot(test_mold_scale$D_R, type = "l",lty=1, lwd=2)
lines(test_mold_scale$pred_D_R_reg_scale[,1], type="l", col = "red",lty=1, lwd=2)
legend(x=40, y=1200, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)

MSE_reg_scale <- mean((test_mold_scale$D_R - test_mold_scale$pred_D_R_reg_scale[,1])^2)
MSE_reg_scale

#2.2.2 svm_scale
reg_model_svm_scale <- svm(D_R ~ N2 + NH3 + SiH4 + Pres + HF + LF + Gap, data=train_mold_scale, gamma=1, cost=16)
summary(reg_model_svm_scale)

pred_D_R_svm_scale <- predict(reg_model_svm_scale, test_mold_scale, interval = "confidence")
test_mold_scale$pred_D_R_svm_scale <- pred_D_R_svm_scale

plot(test_mold_scale$D_R, type = "l",lty=1, lwd=2)
lines(test_mold_scale$pred_D_R_svm_scale, type="l", col = "red",lty=1, lwd=2)
legend(x=40, y=1200, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)


#########################################################################################

# 3. R_I
# 3.1
#reg_model_R_I <- lm(R_I ~ Temp + N2 + NH3 + SiH4 + HF, data=train_mold)
reg_model_R_I <- lm(R_I ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(reg_model_R_I)

pred_R_I_reg <- predict(reg_model_R_I, test_mold, interval = "confidence")
test_mold$pred_R_I_reg <- pred_R_I_reg

plot(test_mold$R_I, type = "l",lty=1, lwd=2)
lines(test_mold$pred_R_I_reg[,1], type="l", col = "red",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)

reg_R_I_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$R_I - test_mold$pred_R_I_reg[,1])/test_mold$R_I))
reg_R_I_MAPE
#3.2
#model_svm_R_I <- svm(R_I ~ Temp + N2 + NH3 + SiH4 + HF, data=train_mold)
model_svm_R_I <- svm(R_I ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(model_svm_R_I)

pred_R_I_svm <- predict(model_svm_R_I, test_mold, interval = "confidence")
test_mold$pred_R_I_svm <- pred_R_I_svm

plot(test_mold$R_I, type = "l",lty=1, lwd=2)
lines(test_mold$pred_R_I_svm, type="l", col = "blue",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "blue"), lty = 1, lwd=3, cex=1)

svm_R_I_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$R_I - test_mold$pred_R_I_svm)/test_mold$R_I))

svm_R_I_MAPE


#########################################################################################

# 4. Stress
# 4.1
#reg_model_R_I <- lm(R_I ~ Temp + N2 + NH3 + SiH4 + HF, data=train_mold)
reg_model_stress <- lm(stress ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(reg_model_stress)

pred_stress_reg <- predict(reg_model_stress, test_mold, interval = "confidence")
test_mold$pred_stress_reg <- pred_stress_reg

plot(test_mold$stress, type = "l",lty=1, lwd=2)
lines(test_mold$pred_stress_reg[,1], type="l", col = "red",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)


reg_stress_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$stress - test_mold$pred_stress_reg[,1])/test_mold$stress))
reg_stress_MAPE
#3.2

model_svm_stress <- svm(stress ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(model_svm_stress)

pred_stress_svm <- predict(model_svm_stress, test_mold, interval = "confidence")
test_mold$pred_stress_svm <- pred_stress_svm

plot(test_mold$stress, type = "l",lty=1, lwd=2)
lines(test_mold$pred_stress_svm, type="l", col = "blue",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "blue"), lty = 1, lwd=3, cex=1)

svm_stress_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$stress - test_mold$pred_stress_svm)/test_mold$stress))
svm_stress_MAPE


#########################################################################################

# 4. Unif
# 4.1

reg_model_Unif <- lm(Unif ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(reg_model_Unif)

pred_Unif_reg <- predict(reg_model_Unif, test_mold, interval = "confidence")
test_mold$pred_Unif_reg <- pred_Unif_reg

plot(test_mold$Unif, type = "l",lty=1, lwd=2, ylim = c(0,6))
lines(test_mold$pred_Unif_reg[,1], type="l", col = "red",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "red"), lty = 1, lwd=3, cex=1)

reg_Unif_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$stress - test_mold$pred_stress_reg[,1])/test_mold$stress))
reg_Unif_MAPE
#4.2

model_svm_Unif <- svm(Unif ~ N2 + NH3 + SiH4 + Pres+ HF + Gap, data=train_mold)
summary(model_svm_Unif)

pred_Unif_svm <- predict(model_svm_Unif, test_mold, interval = "confidence")
test_mold$pred_Unif_svm <- pred_Unif_svm

plot(test_mold$Unif, type = "l",lty=1, lwd=2)
lines(test_mold$pred_Unif_svm, type="l", col = "blue",lty=1, lwd=2)
legend(x=140, y=1.96, c("D_R","Predict"), col = c("black", "blue"), lty = 1, lwd=3, cex=1)

svm_Unif_MAPE = 100/nrow(test_mold) * sum(abs((test_mold$Unif - test_mold$pred_Unif_svm)/test_mold$R_I))
svm_Unif_MAPE








#5. Virtual 

test_LMOLD <- read.csv("testLMOLD_2.csv")

test_D_R_reg <- predict(reg_model_D_R, test_LMOLD, interval = "confidence")
test_LMOLD$test_D_R_reg <- test_D_R_reg

test_D_R_svm <- predict(model_svm, test_LMOLD, interval = "confidence")
test_LMOLD$test_D_R_svm <- test_D_R_svm


test_R_I_reg <- predict(reg_model_R_I, test_LMOLD, interval = "confidence")
test_LMOLD$test_R_I_reg <- test_R_I_reg

test_R_I_svm <- predict(model_svm_R_I, test_LMOLD, interval = "confidence")
test_LMOLD$test_R_I_svm <- test_R_I_svm


test_stress_reg <- predict(reg_model_stress, test_LMOLD, interval = "confidence")
test_LMOLD$test_stress_reg <- test_stress_reg

test_stress_svm <- predict(model_svm_stress, test_LMOLD, interval = "confidence")
test_LMOLD$test_stress_svm <- test_stress_svm


test_Unif_reg <- predict(reg_model_Unif, test_LMOLD, interval = "confidence")
test_LMOLD$test_Unif_reg <- test_Unif_reg

test_Unif_svm <- predict(model_svm_Unif, test_LMOLD, interval = "confidence")
test_LMOLD$test_Unif_svm <- test_Unif_svm



write.table(test_LMOLD, "C:/Users/wtjang/Documents/work/20190319_result.csv", 
            sep = ",", row.names = FALSE, quote = FALSE, append = TRUE,  na = "NA")



val <- test_LMOLD

val <- subset(val, val$test_D_R_svm >=1700)

val <- subset(val, val$test_R_I_svm < 1.89)

val <- subset(val, val$test_stress_svm > 450)

val <- subset(val, val$test_stress_svm < 600)



write.table(val, "C:/Users/wtjang/Documents/work/val_1.csv", 
            sep = ",", row.names = FALSE, quote = FALSE, append = TRUE,  na = "NA")



# test D/R MAPE
plot(test_LMOLD$D_R, type = "l",lty=1, lwd=2)
lines(test_LMOLD$test_D_R_reg[,1], type="l", col = "red",lty=1, lwd=2)
lines(test_LMOLD$test_D_R_svm, type="l", col = "blue",lty=1, lwd=2)

test_reg_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$D_R - test_LMOLD$test_D_R_reg[,1])/test_LMOLD$D_R))
test_svm_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$D_R - test_LMOLD$test_D_R_svm)/test_LMOLD$D_R))

test_reg_MAPE
test_svm_MAPE

# test R/I MAPE
plot(test_LMOLD$R_I, type = "l",lty=1, lwd=2)
lines(test_LMOLD$test_R_I_reg[,1], type="l", col = "red",lty=1, lwd=2)
lines(test_LMOLD$test_R_I_svm, type="l", col = "blue",lty=1, lwd=2)

test_R_I_reg_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$R_I - test_LMOLD$test_R_I_reg[,1])/test_LMOLD$R_I))
test_R_I_svm_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$R_I - test_LMOLD$test_R_I_svm)/test_LMOLD$R_I))

test_R_I_reg_MAPE
test_R_I_svm_MAPE

# test Stress MAPE
plot(test_LMOLD$stress, type = "l",lty=1, lwd=2)
lines(test_LMOLD$test_stress_reg[,1], type="l", col = "red",lty=1, lwd=2)
lines(test_LMOLD$test_stress_svm, type="l", col = "blue",lty=1, lwd=2)

test_stress_reg_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$stress - test_LMOLD$test_stress_reg[,1])/test_LMOLD$stress))
test_stress_svm_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$stress - test_LMOLD$test_stress_svm)/test_LMOLD$stress))

test_stress_reg_MAPE
test_stress_svm_MAPE

# test Stress MAPE
plot(test_LMOLD$Unif, type = "l",lty=1, lwd=2)
lines(test_LMOLD$test_Unif_reg[,1], type="l", col = "red",lty=1, lwd=2)
lines(test_LMOLD$test_Unif_svm, type="l", col = "blue",lty=1, lwd=2)

test_Unif_reg_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$Unif - test_LMOLD$test_Unif_reg[,1])/test_LMOLD$Unif))
test_Unif_svm_MAPE = 100/nrow(test_LMOLD) * sum(abs((test_LMOLD$Unif - test_LMOLD$test_Unif_svm)/test_LMOLD$Unif))

test_Unif_reg_MAPE
test_Unif_svm_MAPE


