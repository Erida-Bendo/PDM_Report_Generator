
class LatexContent:

  
  def createRevisionTable(page_type, rev_num, description, author_init, date_number, checker_init, dates, revText):
    if page_type=="A4":
      if (dates):
        table=r"""
\begin{longtable}{@{\extracolsep{\fill}}p{0.15\textwidth}p{0.35\textwidth}p{0.15\textwidth}p{0.15\textwidth}p{0.15\textwidth}@{}}
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline
\endfirsthead
\hline
\multicolumn{5}{@{}c@{}}{} \\
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline
\endhead
\hline
\multicolumn{5}{r}{} \\

\endfoot"""

        for i in range(len(dates)):
          table+=r""" 
\parbox[t]{0.15\textwidth}{\raggedright """ + str(revText[i]) + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + str(dates[i]) + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[1.75ex]
\hline"""
        table+=r"""
\parbox[t]{0.15\textwidth}{\raggedright """ + rev_num + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + date_number + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[1.75ex]
\hline
\end{longtable}"""
      else:
        table=r"""
\begin{longtable}{@{\extracolsep{\fill}}p{0.15\textwidth}p{0.35\textwidth}p{0.15\textwidth}p{0.15\textwidth}p{0.15\textwidth}@{}}
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline
\endfirsthead
\hline
\multicolumn{5}{@{}c@{}}{} \\
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline
\endhead
\hline
\multicolumn{5}{r}{} \\

\endfoot

\parbox[t]{0.15\textwidth}{\raggedright """ + rev_num + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + date_number + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[3.75ex]
\hline
\end{longtable}
  """

    elif page_type == "A3":
      if (dates):
        table=r"""
\begin{longtable}{@{\extracolsep{\fill}}p{0.15\textwidth}p{0.35\textwidth}p{0.15\textwidth}p{0.15\textwidth}p{0.15\textwidth}@{}}
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline"""
        for i in range(len(dates)):
          table+=r""" 
\parbox[t]{0.15\textwidth}{\raggedright """ + str(revText[i]) + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + str(dates[i]) + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[1.75ex]
\hline          
"""
        table+=r"""
        \parbox[t]{0.15\textwidth}{\raggedright """ + rev_num + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + date_number + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[1.75ex]
\hline
\end{longtable}"""
      else:
        table=r"""
\begin{longtable}{@{\extracolsep{\fill}}p{0.15\textwidth}p{0.35\textwidth}p{0.15\textwidth}p{0.15\textwidth}p{0.15\textwidth}@{}}
\textbf{Revision} & \textbf{Beschreibung} & \textbf{Autor} & \textbf{Datum} & \textbf{geprüft} \\
\hline
\parbox[t]{0.15\textwidth}{\raggedright """ + rev_num + r"""} & \parbox[t]{0.35\textwidth}{\raggedright """ + description + r"""} & \parbox[t]{0.15\textwidth}{\raggedright """ + author_init + r"""} & """ + date_number + r""" & \parbox[t]{0.15\textwidth}{\raggedright """ + checker_init + r"""} \\
[3.75ex]
\hline
\end{longtable}
"""
    
    return table
    
  @staticmethod
  def content(logo_fp, date_number, date_month, proj_name,report_name,proj_code,proj_num,rev_num,author, description, checker,author_init, checker_init,author_email, page_type, dates, revText):
    table=LatexContent.createRevisionTable(page_type, rev_num, description, author_init, date_number, checker_init,  dates, revText)
    if page_type == "A4":
      content = r"""
\documentclass[9pt,""" + page_type.lower() + r"""paper]{report}
\usepackage{graphicx}
\usepackage{fontspec}
\usepackage{float}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{mwe}
\usepackage{adjustbox}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{makecell}
\usepackage{hyperref}
\usepackage[usegeometry]{typearea}
\usepackage[vmargin=1.28in,hmargin=1in]{geometry}
\usepackage{ragged2e}
\usepackage{tabularx}
\usepackage{titlesec}
\usepackage[ngerman]{babel}
\patchcmd{\chapter}{\thispagestyle{plain}}{\thispagestyle{fancy}}{}{}
\renewcommand\tabularxcolumn[1]{m{#1}}
\setmainfont{Segoe UI Symbol}
\defaultfontfeatures{Ligatures=TeX}
\setsansfont{Segoe UI}
\setmainfont{Segoe UI}

\definecolor{greenish}{rgb}{0.769,0.839,0}
\definecolor{black}{rgb}{0,0,0}

\titleformat{\chapter}
  {\fontsize{16}{19.2}\selectfont\bfseries\sffamily\color{greenish}}
  {\thechapter}{1em}{}

\titleformat{\section}
  {\fontsize{10}{12}\selectfont\bfseries\sffamily\color{black}}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\fontsize{10}{12}\selectfont\bfseries\sffamily\color{black}}
  {\thesubsection}{1em}{}

\titleformat{\subsubsection}
  {\fontsize{10}{12}\selectfont\bfseries}
  {\thesubsubsection}{1em}{}

\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}

\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{4}
\begin{document}

\begin{titlepage}
\newgeometry{top=0.75cm, bottom=1.5cm, left=2.5cm, right=2.5cm}
\centering
\includegraphics[width=0.45\textwidth]{""" + logo_fp.replace('\\','/') + r"""}\par\vspace{1cm}
\vspace{8.5cm}
 {{\fontsize{24}{28.8}\bfseries """ + proj_name + r"""\par}}
\vspace{0.3cm}
{{\Large\bfseries """ + report_name + r"""\par}}
\vspace{1cm}
{{\Large\bfseries """ + proj_code + r"""\par}}
\vspace{1cm}
{\fontsize{10}{12} \bfseries """ + proj_num + r"""\par}
\vspace{0.2cm}
{{\fontsize{10}{12}""" + date_month + r"""\par}\par}
\vspace{0.2cm}
{{\fontsize{10}{12} Revision """ + rev_num + r"""\par}\par}
\vspace{5.5cm}
\vfill
{{\footnotesize Copyright\copyright{} 1976 - 2024 BuroHappold Engineering. All Rights Reserved }}
\end{titlepage}

\restoregeometry

\definecolor{myfooterline}{RGB}{196, 214, 0}
\fancypagestyle{myheaderfooter}{
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{3pt}
\renewcommand{\footrule}{\textcolor{myfooterline}{\hrule width\headwidth height\footrulewidth\vskip-\footrulewidth}}
\fancyhead[R]{\fontsize{7}{10}\selectfont \textbf{BURO HAPPOLD}}
\fancyhead[L]{\fontsize{7}{10}\selectfont \textbf{""" + proj_name + r"""}}
\fancyfoot[L]{\fontsize{7}{10}\selectfont\\ """ + proj_code + """ \\\\""" + report_name + r"""\\ Copyright\copyright{} 1976 - 2024 BuroHappold Engineering. All Rights Reserved.}
\fancyfoot[R]{\fontsize{7}{10}\selectfont\\ Revision """ + rev_num + r"""\\ """ + date_month + r"""}
}
\pagestyle{myheaderfooter}
\renewcommand{\arraystretch}{3}
"""+table +r"""

\vspace{1cm}
\section*{Haftungsausschluss Bericht}

Dieser Bericht wurde von Buro Happold GmbH ausschließlich zum alleinigen Nutzen und Gebrauch von """ + proj_name + r""" erstellt. Der Zweck des Berichts umfasst die LP2 Vorentwurfsplanung. Die Haftung von Buro Happold GmbH in Bezug auf die im Bericht enthaltenen Informationen ist nicht auf Dritte ubertragbar. Die Verantwortung von Buro Happold GmbH in Bezug auf den Inhalt des Berichts ist auf den Zweck beschränkt, für den der Bericht erstellt wurde, und unterliegt den ausdrücklichen Vertragsbedingungen mit  useum für Naturkunde Berlin. Der Bericht ist nicht als Anlage oder Finanzberatung auszulegen. Die Ergebnisse dieses Berichts liegen den verfugbaren Informationen zugrunde, wie sie in diesem Bericht dargelegt sind.

\begin{table}[H]
\begin{tabularx}{0.5\textwidth}{@{}X@{\hspace{0.5em}}X@{}}
Autor & """ + author+ r"""\\
\hline
Datum &  """ + date_number + r"""\\
\hline
geprüft & """ + checker+ r"""\\
\hline
Unterschrift & \\
\hline
Datum & """ + date_number + r"""\\
\hline
\end{tabularx}
\end{table}

\newpage
\thispagestyle{empty} % Optional: if you don't want headers/footers on this page
\vspace*{\fill}
\noindent
\begin{flushleft}
\textbf{""" + author+ r"""}\\
Buro Happold GmbH\\
Pfalzburger Straße 43-44\\
10717 Berlin\\
Deutschland\\
T: +49 (0)30 860 9060\\
Email: """ + author_email + r"""
\end{flushleft}
\vspace*{\fill}
\newpage

\end{document}
"""
    elif page_type == "A3":
      content = r"""
\documentclass[9pt]{article}
\usepackage{graphicx}
\usepackage{fontspec}
\usepackage{float}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{mwe}
\usepackage{adjustbox}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{makecell}
\usepackage{hyperref}
\usepackage{ragged2e}
\usepackage{tabularx}
\usepackage{titlesec}
\usepackage[ngerman]{babel}
\usepackage[vmargin=1.28in,hmargin=1in,""" + page_type.lower() + r"""paper,landscape]{geometry}

\renewcommand\tabularxcolumn[1]{m{#1}}
\setmainfont{Segoe UI Symbol}
\defaultfontfeatures{Ligatures=TeX}
\setsansfont{Segoe UI}
\setmainfont{Segoe UI}

\definecolor{greenish}{rgb}{0.769,0.839,0}
\definecolor{black}{rgb}{0,0,0}

\titleformat{\section}
  {\fontsize{10}{12}\selectfont\bfseries\sffamily\color{black}}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\fontsize{10}{12}\selectfont\bfseries\sffamily\color{black}}
  {\thesubsection}{1em}{}


\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}

\definecolor{myfooterline}{RGB}{196, 214, 0}
\fancypagestyle{myheaderfooter}{
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{3pt}
\renewcommand{\footrule}{\textcolor{myfooterline}{\hrule width\headwidth height\footrulewidth\vskip-\footrulewidth}}
\fancyhead[R]{\fontsize{7}{10}\selectfont \textbf{BURO HAPPOLD}}
\fancyhead[L]{\fontsize{7}{10}\selectfont \textbf{""" + proj_name + r"""}}
\fancyfoot[L]{\fontsize{7}{10}\selectfont\\ """ + proj_code + """ \\\\""" + report_name + r"""\\ Copyright\copyright{} 1976 - 2024 BuroHappold Engineering. All Rights Reserved.}
\fancyfoot[R]{\fontsize{7}{10}\selectfont\\ Revision """ + rev_num + r"""\\ """ + date_month + r"""}
}

\begin{document}
\pagenumbering{gobble}
\begin{titlepage}
\hfill
\begin{minipage}{0.45\textwidth}
\centering
\includegraphics[width=0.45\textwidth]{""" + logo_fp.replace('\\','/') + r"""}\par\vspace{1cm}
\vspace{8.5cm}
 {{\fontsize{24}{28.8}\bfseries """ + proj_name + r"""\par}}
\vspace{0.3cm}
{{\Large\bfseries """ + report_name + r"""\par}}
\vspace{1cm}
{{\Large\bfseries """ + proj_code + r"""\par}}
\vspace{1cm}
{\fontsize{10}{12} \bfseries """ + proj_num + r"""\par}
\vspace{0.2cm}
{{\fontsize{10}{12}""" + date_month + r"""\par}\par}
\vspace{0.2cm}
{{\fontsize{10}{12} Revision """ + rev_num + r"""\par}\par}
\vspace{5.5cm}
\vfill
{{\footnotesize Copyright\copyright{} 1976 - 2024 BuroHappold Engineering. All Rights Reserved }}
\end{minipage}
\end{titlepage}

% Second page
\pagestyle{myheaderfooter}
\begin{minipage}[t]{0.5\textwidth}
\renewcommand{\arraystretch}{3}
"""+table+r"""
\vspace{1cm}
\section*{Haftungsausschluss Bericht}

Dieser Bericht wurde von Buro Happold GmbH ausschließlich zum alleinigen Nutzen und Gebrauch von """ + proj_name + r""" erstellt. Der Zweck des Berichts umfasst die LP2 Vorentwurfsplanung. Die Haftung von Buro Happold GmbH in Bezug auf die im Bericht enthaltenen Informationen ist nicht auf Dritte ubertragbar. Die Verantwortung von Buro Happold GmbH in Bezug auf den Inhalt des Berichts ist auf den Zweck beschränkt, für den der Bericht erstellt wurde, und unterliegt den ausdrücklichen Vertragsbedingungen mit  useum für Naturkunde Berlin. Der Bericht ist nicht als Anlage oder Finanzberatung auszulegen. Die Ergebnisse dieses Berichts liegen den verfugbaren Informationen zugrunde, wie sie in diesem Bericht dargelegt sind.

\begin{table}[H]
\begin{tabularx}{0.5\textwidth}{@{}X@{\hspace{0.5em}}X@{}}
Autor & """ + author+ r"""\\
\hline
Datum &  """ + date_number + r"""\\
\hline
geprüft & """ + checker+ r"""\\
\hline
Unterschrift & \\
\hline
Datum & """ + date_number + r"""\\
\hline
\end{tabularx}
\end{table}
\end{minipage}
\newpage
\pagestyle{empty}
% Third page
\begin{minipage}[t]{0.5\textwidth}
\null
\vspace*{0.35\paperheight}
\begin{center}
\begin{flushleft}
\textbf{""" + author+ r"""}\\
Buro Happold GmbH\\
Pfalzburger Straße 43-44\\
10717 Berlin\\
Deutschland\\
T: +49 (0)30 860 9060\\
Email: """ + author_email + r"""
\end{flushleft}
\end{center}
\end{minipage}

\end{document}
"""      

    return content
