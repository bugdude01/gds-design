# Just a small note!

## regarding the requirements.txt file

You may find that you have an inssue installing on a windows system where you come accross 
problems installing rcssmin due to C++. THe error message will read something like this:

>building '_rcssmin' extension

>error: Microsoft Visual C++ 10.0 is required. Get it with "Microsoft Windows SDK 7.1": www.microsoft.com/download/details.aspx?id=8279

Best way froward initially, just to get rolling with your development environment is to do
the following:

```pip install rcssmin --install-option="--without-c-extensions"```

You MAY get the same issue with rjsmin - if so:

```pip install rjsmin --install-option="--without-c-extensions"```

and then the usual ```pip install -r requirements.txt``` should install your remaining files.

## Bon Chance!!

