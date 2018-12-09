#pragma once
#include "TitleBar.h"
#include <QVBoxLayout>
#include <QFile>
#include <QException>
#include <QtDebug>

class MainWindow : public QMainWindow
{
	Q_OBJECT

private:
	TitleBar *titleBar;
	QWidget *centerWidget;
	QWidget *clientWidget;
	QVBoxLayout *lay;

private:
	void InitializeWindow();
	void InitializeViews();
	QString LoadStyleFromQSS(const QString &str);

public:
	MainWindow(QWidget *parent = Q_NULLPTR);

private:
	
};
