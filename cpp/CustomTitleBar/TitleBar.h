#pragma once
#include <QtWidgets>
#include <QHBoxLayout>
#include "default.h"
#include <QMouseEvent>
#include <QPoint>

class TitleBar :
	public QWidget
{
private:
	QLabel *titleLabel;
	QLabel *iconLabel;
	QPushButton *minButton;
	QPushButton *restoreButton;
	QPushButton *closeButton;
	QHBoxLayout *lay;

	QWidget *win;

	bool isPressed;
	QPoint startPos;

private:
	void InitializeWidget();
	void InitializeViews();

private slots:
	void ShowRestoreWindow();
	void ShowMaximizedWindow();
	void ShowMinimizedWindow();
	void CloseWindow();

public:
	void mouseDoubleClickEvent(QMouseEvent *event);
	void mousePressEvent(QMouseEvent *event);
	void mouseReleaseEvent(QMouseEvent *event);
	void mouseMoveEvent(QMouseEvent *event);

public:
	TitleBar(QWidget *parent = nullptr);
	virtual ~TitleBar();

public:
	void SetTitle(const QString &str);
	void SetIcon(QPixmap &pix);
};

