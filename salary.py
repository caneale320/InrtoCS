# Caleb Neale, can4ku
import urllib.request
import re


def name_to_URL(name):
    name = name.lower()
    if "," in name:
        splitname = name.split(",")
        for i in range(len(splitname)):
            splitname[i] = splitname[i].strip()
        url = splitname[1] + "-" + splitname[0]
        return url
    elif " " in name:
        return name.replace(" ", "-")
    else:
        url = name
        return url


def report(name):
    try:
        url = "http://cs1110.cs.virginia.edu/files/uva2016/" + name_to_URL(name)
        stream = urllib.request.urlopen(url)

        jobtitle = re.compile(r"Job title:\s([\w\s\W]+)<br /> 2016")
        totalcomp = re.compile(r"total gross pay: \$([0-9]{1,3},[0-9]{1,3})")
        rankreg = re.compile(r"rank</td><td>([0-9]?,?[0-9]{1,3})")

        for line in stream:
            decodedline = line.decode("UTF-8").strip()
            jobmatches = jobtitle.finditer(decodedline)
            if jobmatches is not None:
                for match in jobmatches:
                    jobmatches = match
                    job = match.group(1)
                    if "&amp;" in job:
                        job = job.replace("&amp;", "&")
                    if "&lt" in job:
                        job = job.replace("&lt;", "<")
                    if "&gt" in job:
                        job = job.replace("&gt;", ">")

            compmatches = totalcomp.finditer(decodedline)
            if compmatches is not None:
                for match in compmatches:
                    compmatches = match
                    salary = match.group(1)
                    salary = float(salary.replace(",", ""))

            rankmatches = rankreg.finditer(decodedline)
            if rankmatches is not None:
                for match in rankmatches:
                    rankmatches = match
                    rank = int(rankmatches.group(1).replace(",", ""))

        return job, salary, rank

    except:
        job = None
        salary = 0
        rank = 0

        return job, salary, rank


for name in (
        'Lewis Lloyd',
        'Sullivan, Teresa',
        '161048349',
        'Ali Reza Forghani Esfahani',
        'pamela-neff',
        'Thomas Jefferson'
        ):
    job, money, rank = report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')