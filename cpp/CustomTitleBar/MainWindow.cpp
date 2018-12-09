#include "MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
	: QMainWindow(parent)
{
	InitializeWindow();
}

void MainWindow::InitializeWindow()
{
	setWindowFlags(Qt::FramelessWindowHint);
	setMinimumSize(WIN_DEFAULT_WIDTH, WIN_DEFAULT_HEIGHT);
	InitializeViews();
	setStyleSheet(LoadStyleFromQSS(WINDOW_QSS));
}

void MainWindow::InitializeViews()
{
	titleBar = new TitleBar(this);
	clientWidget = new QWidget(this);
	centerWidget = new QWidget(this);
	setCentralWidget(centerWidget);

	lay = new QVBoxLayout(this);
	centerWidget->setLayout(lay);

	lay->addWidget(titleBar);
	lay->addWidget(clientWidget);
	lay->setStretch(1, 100);
	lay->setSpacing(0);
	lay->setMargin(0);

	titleBar->SetIcon(QPixmap(WINDOW_ICON));
	titleBar->SetTitle(WINDOW_TITLE);
}

QString MainWindow::LoadStyleFromQSS(const QString &str)
{
	QString line;
	try
	{
		QFile file(str);
		file.open(QFile::ReadOnly);

		line = file.readAll();
		file.close();
	}
	catch (const QException& e)
	{
		qDebug() << __FUNCTION__ << __LINE__ << e.what();
		return line;
	}

	return line;
}
