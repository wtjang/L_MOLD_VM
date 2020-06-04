

library(ggplot2)
library(readxl)
library(dplyr)


df <- read_xlsx("crack.xlsx")

df$Crack_Type <- as.factor(df$Crack_Type)
df$RF_IMS <- as.factor(df$RF_IMS)
df$UDT_target_1.05 <- as.factor(df$UDT_target_1.05)
df$PID_change <- as.factor(df$PID_change)
df$Process <- as.factor(df$Process)

df$Equipment <- as.factor(df$Equipment)
df$Chamber <- as.factor(df$Chamber)


# 1. Crack Type

ggplot(data = df, aes(x=Use_Period, y = WFS, color = Crack_Type)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

my2cols <- c("#00BFC4", "#F8766D")

scatterPlot <- ggplot(df, aes(Use_Period, WFS)) + geom_point(aes(color = Crack_Type),cex=3) + 
  scale_color_manual(values = my2cols) + theme(legend.position=c(0,1), legend.justification=c(0,1)) +
  theme(axis.text = element_text(size = rel(1.5)))

#options(scipen=100)
xdensity <- ggplot(df, aes(Use_Period)) + geom_density(aes(fill = as.factor(Crack_Type)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + theme(axis.text = element_text(size = rel(1.5)))

require(scales)
ydensity <- ggplot(df, aes(WFS)) + geom_density(aes(fill=as.factor(Crack_Type)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + coord_flip() + theme(axis.text = element_text(size = rel(1.5))) + scale_y_continuous(labels = comma)

blankPlot <- ggplot()+geom_blank()+ theme_void()

require("gridExtra") 
grid.arrange(xdensity,blankPlot,scatterPlot, ydensity, ncol=2, nrow=2, widths=c(4, 1.4), heights=c(1.4, 4))

# 2. RF_IMS

ggplot(data = df, aes(x=Use_Period, y = WFS, color = RF_IMS)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

my2cols <- c("#00BFC4", "#F8766D")

scatterPlot <- ggplot(df, aes(Use_Period, WFS)) + geom_point(aes(color = RF_IMS),cex=3) + 
  scale_color_manual(values = my2cols) + theme(legend.position=c(0,1), legend.justification=c(0,1)) +
  theme(axis.text = element_text(size = rel(1.5)))

#options(scipen=100)
xdensity <- ggplot(df, aes(Use_Period)) + geom_density(aes(fill = as.factor(RF_IMS)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + theme(axis.text = element_text(size = rel(1.5)))

require(scales)
ydensity <- ggplot(df, aes(WFS)) + geom_density(aes(fill=as.factor(RF_IMS)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + coord_flip() + theme(axis.text = element_text(size = rel(1.5))) + scale_y_continuous(labels = comma)

blankPlot <- ggplot()+geom_blank()+ theme_void()

require("gridExtra") 
grid.arrange(xdensity,blankPlot,scatterPlot, ydensity, ncol=2, nrow=2, widths=c(4, 1.4), heights=c(1.4, 4))


# 3. UDT_target_1.05
df_UDT <- df %>% filter(df$UDT_target_1.05 == 'O' | df$UDT_target_1.05 == 'X') # 405

ggplot(data = df_UDT, aes(x=Use_Period, y = WFS, color = UDT_target_1.05)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

my2cols <- c("#00BFC4", "#F8766D")

scatterPlot <- ggplot(df_UDT, aes(Use_Period, WFS)) + geom_point(aes(color = UDT_target_1.05),cex=3) + 
  scale_color_manual(values = my2cols) + theme(legend.position=c(0,1), legend.justification=c(0,1)) +
  theme(axis.text = element_text(size = rel(1.5)))

#options(scipen=100)
xdensity <- ggplot(df_UDT, aes(Use_Period)) + geom_density(aes(fill = as.factor(UDT_target_1.05)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + theme(axis.text = element_text(size = rel(1.5)))

require(scales)
ydensity <- ggplot(df_UDT, aes(WFS)) + geom_density(aes(fill=as.factor(UDT_target_1.05)), alpha=.8) + 
  scale_fill_manual(values = my2cols) + theme(legend.position = "none") + coord_flip() + theme(axis.text = element_text(size = rel(1.5))) + scale_y_continuous(labels = comma)

blankPlot <- ggplot()+geom_blank()+ theme_void()

require("gridExtra") 
grid.arrange(xdensity,blankPlot,scatterPlot, ydensity, ncol=2, nrow=2, widths=c(4, 1.4), heights=c(1.4, 4))


# 4. PID_Change


ggplot(data = df, aes(x=Use_Period, y = WFS, color = PID_change)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))


my3cols <- c("#7CAE00", "#00BFC4", "#F8766D")

scatterPlot <- ggplot(df_UDT, aes(Use_Period, WFS)) + geom_point(aes(color = PID_change),cex=3) + 
  scale_color_manual(values = my3cols) + theme(legend.position=c(0,1), legend.justification=c(0,1)) +
  theme(axis.text = element_text(size = rel(1.5)))

#options(scipen=100)
xdensity <- ggplot(df_UDT, aes(Use_Period)) + geom_density(aes(fill = as.factor(PID_change)), alpha=.8) + 
  scale_fill_manual(values = my3cols) + theme(legend.position = "none") + theme(axis.text = element_text(size = rel(1.5)))

require(scales)
ydensity <- ggplot(df_UDT, aes(WFS)) + geom_density(aes(fill=as.factor(PID_change)), alpha=.8) + 
  scale_fill_manual(values = my3cols) + theme(legend.position = "none") + coord_flip() + theme(axis.text = element_text(size = rel(1.5))) + scale_y_continuous(labels = comma)

blankPlot <- ggplot()+geom_blank()+ theme_void()

require("gridExtra") 
grid.arrange(xdensity,blankPlot,scatterPlot, ydensity, ncol=2, nrow=2, widths=c(4, 1.4), heights=c(1.4, 4))







# 5. Process

ggplot(data = df, aes(x=Use_Period, y = WFS, color = Process)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15)) + stat_smooth(method=lm) 

my5cols <- c("#F8766D", "#7E6148B2","#7CAE00", "#00BFC4", "#C77CFF")

scatterPlot <- ggplot(df, aes(Use_Period, WFS)) + geom_point(aes(color = Process),cex=3) + 
  scale_color_manual(values = my5cols) + theme(legend.position=c(0,1), legend.justification=c(0,1)) +
  theme(axis.text = element_text(size = rel(1.5)))

#options(scipen=100)
xdensity <- ggplot(df, aes(Use_Period)) + geom_density(aes(fill = as.factor(Process)), alpha=.8) + 
  scale_fill_manual(values = my5cols) + theme(legend.position = "none") + theme(axis.text = element_text(size = rel(1.5)))

require(scales)
ydensity <- ggplot(df, aes(WFS)) + geom_density(aes(fill=as.factor(Process)), alpha=.8) + 
  scale_fill_manual(values = my5cols) + theme(legend.position = "none") + coord_flip() + theme(axis.text = element_text(size = rel(1.5))) + scale_y_continuous(labels = comma)

blankPlot <- ggplot()+geom_blank()+ theme_void()

require("gridExtra") 
grid.arrange(xdensity,blankPlot,scatterPlot, ydensity, ncol=2, nrow=2, widths=c(4, 1.4), heights=c(1.4, 4))


# 6. Equipment

ggplot(data = df, aes(x=Use_Period, y = WFS, color = Equipment)) +
  geom_point(stat = 'identity', cex = 3) +
  theme(panel.grid.major = element_line(color = "grey80" )) +
  theme(axis.text = element_text(size = rel(1.5))) +
  xlab("Use_Period") + ylab("WFS") + 
  theme(legend.text = element_text(size = 14)) +
  theme(legend.title = element_text(size = 14)) + 
  theme(axis.title = element_text(size = 15))


# 7. Decision Tree 

df_tree <- read_xlsx("crack_tree.xlsx")
library(caret)

df_tree$Equipment <- as.factor(df_tree$Equipment)

set.seed(1000) #reproducability setting
intrain<-createDataPartition(y=df_tree$Equipment, p=0.7, list=FALSE) 
train<-df_tree[intrain, ]
test<-df_tree[-intrain, ]

library(rpart)
rpartmod <- rpart(Equipment~., data=train, method = "class")
plot(rpartmod)
text(rpartmod)
printcp(rpartmod)
plotcp(rpartmod)

rpartpred<-predict(rpartmod, test, type='class')
confusionMatrix(rpartpred, test$Equipment)
