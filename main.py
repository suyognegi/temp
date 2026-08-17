from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from playwright.async_api import async_playwright
import asyncio
import base64
import json
import random
import time


# months_={'sep':'https://leetcode.com/static/images/badges/dcc-2025-9.png','oct':'https://leetcode.com/static/images/badges/dcc-2025-10.png','nov':'https://leetcode.com/static/images/badges/dcc-2025-11.png','dec':'https://leetcode.com/static/images/badges/dcc-2025-12.png',
#          'jan':'https://leetcode.com/static/images/badges/dcc-2026-1.png','feb':'https://leetcode.com/static/images/badges/dcc-2026-2.png',
#          'mar':'https://leetcode.com/static/images/badges/dcc-2026-3.png','apr':'https://leetcode.com/static/images/badges/dcc-2026-4.png',
#          'may':'https://leetcode.com/static/images/badges/dcc-2026-5.png','jun':'https://leetcode.com/static/images/badges/dcc-2026-6.png',
#          'jul':'https://leetcode.com/static/images/badges/dcc-2026-7.png','aug':'https://leetcode.com/static/images/badges/dcc-2026-10.png',
#          }
async def r():
    a = ["shadow", "void", "pixel", "ghost", "neon", "cyber", "dark", "silent", "chaos", "glitch", "nova",
         "ember", "lunar", "drift", "cipher", "orbit"]
    b = ["dev", "user", "coder", "lurker", "poster", "kid", "bot", "wizard", "runner", "agent", "meme", "sigma",
         "alt", "404", "xd"]
    return random.choice(a) + "_" + random.choice(b) + str(random.randint(0, 23))


change_ = 1
months_ = {
    9: 'https://leetcode.com/static/images/badges/dcc-2025-9.png',
    10: 'https://leetcode.com/static/images/badges/dcc-2025-10.png',
    11: 'https://leetcode.com/static/images/badges/dcc-2025-11.png',
    12: 'https://leetcode.com/static/images/badges/dcc-2025-12.png',
    1: 'https://leetcode.com/static/images/badges/dcc-2026-1.png',
    2: 'https://leetcode.com/static/images/badges/dcc-2026-2.png',
    3: 'https://leetcode.com/static/images/badges/dcc-2026-3.png',
    4: 'https://leetcode.com/static/images/badges/dcc-2026-4.png',
    5: 'https://leetcode.com/static/images/badges/dcc-2026-5.png',
    6: 'https://leetcode.com/static/images/badges/dcc-2026-6.png',
    7: 'https://leetcode.com/static/images/badges/dcc-2026-7.png',
    8: 'https://leetcode.com/static/images/badges/dcc-2026-8.png',
}
y = 82.64

spacesof_x = {
    # later do a thing , "caluclate and adjust the x es by add or subtracting by the amount of days left in that month
    0: "8.64",
    1: "64.91",
    2: "126.94",
    3: "194.73000000000002",
    4: "262.52000000000001",
    5: "324.55",
    6: "380.81999999999994",
    7: "437.08999999999986",
    8: "499.1199999999998",
    9: "566.9099999999996",
    10: "634.6999999999995",
    11: "696.7299999999993",
    12: "752.9999999999992"
}


async def get_top_chart_n_stuff_const():
    rank = random.randrange(100, 200)
    top_chart_n_stuff_const = f'''
<div class="bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg my-4 hidden h-[200px] w-full p-4 lc-lg:mt-0 lc-xl:flex"><div class="lc-md:min-w-none h-full w-full min-w-[200px] flex-1"><div class="w-full"><div class="relative min-h-[53px] text-xs"><div class="align-start flex w-full"><div class="mr-4"><div class="text-label-3 dark:text-dark-label-3 font-medium">Contest Rating</div><div class="text-label-1 dark:text-dark-label-1 flex items-center text-2xl">2,{rank}</div></div><div class="mr-2 mt-1"><img alt="contest badge" class="h-auto w-full min-w-[30px] max-w-[40px]" data-state="closed" src="/static/images/badges/guardian.png"></div><div class="mr-4"><div class="text-label-3 dark:text-dark-label-3 min-w-[50px] text-xs">Level</div><div class="text-sm leading-[22px] text-blue-s dark:text-dark-blue-s">Guardian</div></div><div class="mr-4"><div class="text-label-3 dark:text-dark-label-3">Global Ranking</div><div class="text-label-1 dark:text-dark-label-1 font-medium leading-[22px]">11,{random.randrange(300, 480)}<span class="text-label-4 dark:text-dark-label-4">/878,139</span></div></div><div class="hidden md:block"><div class="text-label-3 dark:text-dark-label-3">Attended</div><div class="text-label-1 dark:text-dark-label-1 font-medium leading-[22px]">{random.randrange(70, 80)}</div></div></div></div><div class="rating-contest-graph"><div data-highcharts-chart="0" style="overflow: hidden;"><div id="highcharts-w04asvk-0" dir="ltr" style="position: relative; overflow: hidden; width: 385px; height: 123px; text-align: left; line-height: normal; z-index: 0; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); user-select: none; touch-action: manipulation; outline: none;" class="highcharts-container "><svg version="1.1" class="highcharts-root" style="font-family: Helvetica, Arial, sans-serif; font-size: 1rem;" xmlns="http://www.w3.org/2000/svg" width="385" height="123" viewBox="0 0 385 123" role="img" aria-label=""><desc>Created with Highcharts 11.1.0</desc><defs><filter id="highcharts-drop-shadow-0"><feDropShadow dx="1" dy="1" flood-color="#000000" flood-opacity="0.75" stdDeviation="2.5"></feDropShadow></filter><clipPath id="highcharts-w04asvk-1-"><rect x="0" y="0" width="365" height="69" fill="none"></rect></clipPath><clipPath id="highcharts-w04asvk-79-"><rect x="0" y="0" width="365" height="69" fill="none"></rect></clipPath><clipPath id="highcharts-w04asvk-82-"><rect x="10" y="10" width="365" height="69" fill="none"></rect></clipPath><clipPath id="highcharts-w04asvk-83-"><rect x="10" y="10" width="365" height="69" fill="none"></rect></clipPath></defs><rect fill="transparent" class="highcharts-background" filter="none" x="0" y="0" width="385" height="123" rx="0" ry="0"></rect><rect fill="none" class="highcharts-plot-background" x="10" y="10" width="365" height="69" filter="none"></rect><g class="highcharts-grid highcharts-xaxis-grid" data-z-index="1"><path fill="none" stroke="#e6e6e6" stroke-width="0" stroke-dasharray="none" data-z-index="1" class="highcharts-grid-line" d="M 13.5 10 L 13.5 79" opacity="1"></path><path fill="none" stroke="#e6e6e6" stroke-width="0" stroke-dasharray="none" data-z-index="1" class="highcharts-grid-line" d="M 370.5 10 L 370.5 79" opacity="1"></path></g><rect fill="none" class="highcharts-plot-border" data-z-index="1" stroke="#cccccc" stroke-width="0" x="10" y="10" width="365" height="69"></rect><g class="highcharts-axis highcharts-xaxis" data-z-index="2"><path fill="none" class="highcharts-axis-line" stroke="transparent" stroke-width="1" data-z-index="7" d="M 10 79.5 L 375 79.5"></path></g><g class="highcharts-series-group" data-z-index="3" filter="none"><g class="highcharts-series highcharts-series-0 highcharts-line-series" data-z-index="0.1" opacity="1" transform="translate(10,10) scale(1 1)" clip-path="url(#highcharts-w04asvk-79-)"><path fill="none" d="M 3.578431372549 57.891 L 8.2868937048504 56.442 L 12.995356037152 56.028 L 17.703818369453 59.202 L 22.412280701754 56.510999999999996 L 27.120743034056 57.269999999999996 L 31.829205366357 60.03 L 36.537667698658 59.064 L 41.24613003096 57.615 L 45.954592363261 52.854 L 50.663054695562 51.336 L 55.371517027864 51.06 L 60.079979360165 46.713 L 64.788441692466 41.952 L 69.496904024768 37.191 L 74.205366357069 36.294 L 78.91382868937 37.674 L 83.622291021672 39.399 L 88.330753353973 41.331 L 93.039215686275 41.745000000000005 L 97.747678018576 44.988 L 102.45614035088 42.78 L 107.16460268318 42.641999999999996 L 111.87306501548 42.021 L 116.58152734778 43.194 L 121.28998968008 42.435 L 125.99845201238 40.434 L 130.70691434469 39.744 L 135.41537667699 35.466 L 140.12383900929 32.43 L 144.83230134159 32.016 L 149.54076367389 31.188000000000002 L 154.24922600619 33.534 L 158.95768833849 27.738 L 163.66615067079 27.6 L 168.3746130031 26.841 L 173.0830753354 27.668999999999997 L 177.7915376677 26.909999999999997 L 182.5 26.909999999999997 L 187.2084623323 21.804000000000002 L 191.9169246646 22.08 L 196.6253869969 19.250999999999998 L 201.33384932921 15.456000000000003 L 206.04231166151 18.906 L 210.75077399381 18.561 L 215.45923632611 20.769 L 220.16769865841 17.802 L 224.87616099071 16.767000000000003 L 229.58462332301 18.837000000000003 L 234.29308565531 16.215000000000003 L 239.00154798762 17.732999999999997 L 243.71001031992 17.664 L 248.41847265222 13.386000000000003 L 253.12693498452 15.939 L 257.83539731682 14.421 L 262.54385964912 12.213000000000001 L 267.25232198142 12.972000000000001 L 271.96078431373 15.456000000000003 L 276.66924664603 13.799999999999997 L 281.37770897833 12.350999999999999 L 286.08617131063 13.386000000000003 L 290.79463364293 15.732 L 295.50309597523 14.697000000000003 L 300.21155830753 13.869 L 304.92002063983 15.110999999999997 L 309.62848297214 16.628999999999998 L 314.33694530444 18.561 L 319.04540763674 20.354999999999997 L 323.75386996904 20.009999999999998 L 328.46233230134 19.182000000000002 L 333.17079463364 15.317999999999998 L 337.87925696594 15.042000000000002 L 342.58771929825 17.595 L 347.29618163055 15.456000000000003 L 352.00464396285 11.523000000000003 L 356.71310629515 9.314999999999998 L 361.42156862745 8.418" class="highcharts-graph" data-z-index="1" stroke="rgba(255, 161, 22, 1)" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" filter="none"></path><path fill="none" d="M 3.578431372549 57.891 L 8.2868937048504 56.442 L 12.995356037152 56.028 L 17.703818369453 59.202 L 22.412280701754 56.510999999999996 L 27.120743034056 57.269999999999996 L 31.829205366357 60.03 L 36.537667698658 59.064 L 41.24613003096 57.615 L 45.954592363261 52.854 L 50.663054695562 51.336 L 55.371517027864 51.06 L 60.079979360165 46.713 L 64.788441692466 41.952 L 69.496904024768 37.191 L 74.205366357069 36.294 L 78.91382868937 37.674 L 83.622291021672 39.399 L 88.330753353973 41.331 L 93.039215686275 41.745000000000005 L 97.747678018576 44.988 L 102.45614035088 42.78 L 107.16460268318 42.641999999999996 L 111.87306501548 42.021 L 116.58152734778 43.194 L 121.28998968008 42.435 L 125.99845201238 40.434 L 130.70691434469 39.744 L 135.41537667699 35.466 L 140.12383900929 32.43 L 144.83230134159 32.016 L 149.54076367389 31.188000000000002 L 154.24922600619 33.534 L 158.95768833849 27.738 L 163.66615067079 27.6 L 168.3746130031 26.841 L 173.0830753354 27.668999999999997 L 177.7915376677 26.909999999999997 L 182.5 26.909999999999997 L 187.2084623323 21.804000000000002 L 191.9169246646 22.08 L 196.6253869969 19.250999999999998 L 201.33384932921 15.456000000000003 L 206.04231166151 18.906 L 210.75077399381 18.561 L 215.45923632611 20.769 L 220.16769865841 17.802 L 224.87616099071 16.767000000000003 L 229.58462332301 18.837000000000003 L 234.29308565531 16.215000000000003 L 239.00154798762 17.732999999999997 L 243.71001031992 17.664 L 248.41847265222 13.386000000000003 L 253.12693498452 15.939 L 257.83539731682 14.421 L 262.54385964912 12.213000000000001 L 267.25232198142 12.972000000000001 L 271.96078431373 15.456000000000003 L 276.66924664603 13.799999999999997 L 281.37770897833 12.350999999999999 L 286.08617131063 13.386000000000003 L 290.79463364293 15.732 L 295.50309597523 14.697000000000003 L 300.21155830753 13.869 L 304.92002063983 15.110999999999997 L 309.62848297214 16.628999999999998 L 314.33694530444 18.561 L 319.04540763674 20.354999999999997 L 323.75386996904 20.009999999999998 L 328.46233230134 19.182000000000002 L 333.17079463364 15.317999999999998 L 337.87925696594 15.042000000000002 L 342.58771929825 17.595 L 347.29618163055 15.456000000000003 L 352.00464396285 11.523000000000003 L 356.71310629515 9.314999999999998 L 361.42156862745 8.418" data-z-index="2" class="highcharts-tracker-line" stroke-linecap="round" stroke-linejoin="round" stroke="rgba(192,192,192,0.0001)" stroke-width="21"></path></g><g class="highcharts-markers highcharts-series-0 highcharts-line-series highcharts-tracker" data-z-index="0.1" opacity="1" transform="translate(10,10) scale(1 1)" clip-path="none"><path fill="white" d="M 361 11.418 A 3 3 0 1 1 361.0029999995 11.417998500000124 Z" stroke="rgba(229, 231, 235, 1)" stroke-width="1" opacity="1" class="highcharts-point"></path></g></g><text x="193" text-anchor="middle" class="highcharts-title" data-z-index="4" style="font-size: 1.2em; color: rgb(51, 51, 51); font-weight: bold; display: none; fill: rgb(51, 51, 51);" y="25"></text><text x="193" text-anchor="middle" class="highcharts-subtitle" data-z-index="4" style="color: rgb(102, 102, 102); font-size: 0.8em; fill: rgb(102, 102, 102);" y="24"></text><text x="10" text-anchor="start" class="highcharts-caption" data-z-index="4" style="color: rgb(102, 102, 102); font-size: 0.8em; fill: rgb(102, 102, 102);" y="120"></text><g class="highcharts-annotation" opacity="1" data-z-index="6" style="cursor: move;"><g class="highcharts-annotation-shapes" clip-path="url(#highcharts-w04asvk-82-)"></g><g class="highcharts-annotation-labels" transform="translate(0,0)"><g class="highcharts-label highcharts-annotation-label highcharts-no-tooltip" transform="translate(317,7)" filter="none"><path fill="#212224" class="highcharts-label-box highcharts-annotation-label-box" d="M 3.5 0.5 L 36.5 0.5 A 3 3 0 0 1 39.5 3.5 L 39.5 5.417999999999999 L 45.5 11.418 L 39.5 17.418 L 39.5 20.5 A 3 3 0 0 1 36.5 23.5 L 3.5 23.5 A 3 3 0 0 1 0.5 20.5 L 0.5 3.5 A 3 3 0 0 1 3.5 0.5 Z" stroke="rgba(247, 250, 255, 0.18)" stroke-width="1"></path><text x="5" data-z-index="1" y="16" style="color: rgba(239, 241, 246, 0.6); font-size: 0.7em; font-weight: normal; fill: rgba(239, 241, 246, 0.6);">2,{rank}</text></g></g></g><g class="highcharts-legend highcharts-no-tooltip" data-z-index="7" visibility="hidden"><rect fill="none" class="highcharts-legend-box" rx="0" ry="0" stroke="#999999" stroke-width="0" filter="none" x="0" y="0" width="8" height="8"></rect><g data-z-index="1"><g></g></g></g><g class="highcharts-axis-labels highcharts-xaxis-labels" data-z-index="7"><text x="24.419069290161126" style="color: rgba(239, 241, 246, 0.6); cursor: default; font-size: 0.8em; fill: rgba(239, 241, 246, 0.6);" text-anchor="middle" transform="translate(0,0)" y="106" opacity="1">2023</text><text x="360.58093070983887" style="color: rgba(239, 241, 246, 0.6); cursor: default; font-size: 0.8em; fill: rgba(239, 241, 246, 0.6);" text-anchor="middle" transform="translate(0,0)" y="106" opacity="1">2026</text></g><g class="highcharts-control-points" data-z-index="99" clip-path="url(#highcharts-w04asvk-82-)"></g></svg></div></div></div></div></div><div class="h-full w-px mx-4 hidden bg-divider-3 dark:bg-dark-divider-3 lc-md:block"></div><div class="lc-md:min-w-none hidden h-full min-w-[200px] flex-1 lc-md:block"><div class="w-full"><div class="relative min-h-[49px]"><div class="absolute left-0 top-0"><div class="text-label-3 dark:text-dark-label-3 text-xs">Top</div><div class="text-label-1 dark:text-dark-label-1 text-2xl">1.{random.randrange(10, 50)}%</div></div><div class="absolute left-[100px] top-0"><div class="text-label-3 dark:text-dark-label-3 text-xs"></div><div class="text-label-1 dark:text-dark-label-1"></div></div></div><div class="cursor-pointer"><div data-highcharts-chart="2" style="overflow: hidden;"><div id="highcharts-w04asvk-168" dir="ltr" style="position: relative; overflow: hidden; width: 385px; height: 115px; text-align: left; line-height: normal; z-index: 0; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); user-select: none; touch-action: manipulation; outline: none;" class="highcharts-container "><svg version="1.1" class="highcharts-root" style="font-family: Helvetica, Arial, sans-serif; font-size: 1rem;" xmlns="http://www.w3.org/2000/svg" width="385" height="115" viewBox="0 0 385 115" role="img" aria-label=""><desc>Created with Highcharts 11.1.0</desc><defs><filter id="highcharts-drop-shadow-2"><feDropShadow dx="1" dy="1" flood-color="#000000" flood-opacity="0.75" stdDeviation="2.5"></feDropShadow></filter><clipPath id="highcharts-w04asvk-169-"><rect x="0" y="0" width="385" height="115" fill="none"></rect></clipPath><clipPath id="highcharts-w04asvk-193-"><rect x="0" y="0" width="385" height="115" fill="none"></rect></clipPath><clipPath id="highcharts-w04asvk-217-"><rect x="0" y="0" width="385" height="115" fill="none"></rect></clipPath></defs><rect fill="transparent" class="highcharts-background" filter="none" x="0" y="0" width="385" height="115" rx="0" ry="0"></rect><rect fill="none" class="highcharts-plot-background" x="0" y="0" width="385" height="115" filter="none"></rect><rect fill="none" class="highcharts-plot-border" data-z-index="1" stroke="#cccccc" stroke-width="0" x="0" y="0" width="385" height="115"></rect><g class="highcharts-series-group" data-z-index="3" filter="none"><g class="highcharts-series highcharts-series-0 highcharts-column-series highcharts-tracker" data-z-index="0.1" opacity="1" transform="translate(0,0) scale(1 1)" clip-path="url(#highcharts-w04asvk-193-)"><path fill="rgba(255, 255, 255, 0.1)" d="M 5.5 107.5 L 16.5 107.5 A 2 2 0 0 1 18.5 109.5 L 18.5 115.5 A 0 0 0 0 1 18.5 115.5 L 3.5 115.5 A 0 0 0 0 1 3.5 115.5 L 3.5 109.5 A 2 2 0 0 1 5.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 22.5 107.5 L 33.5 107.5 A 2 2 0 0 1 35.5 109.5 L 35.5 115.5 A 0 0 0 0 1 35.5 115.5 L 20.5 115.5 A 0 0 0 0 1 20.5 115.5 L 20.5 109.5 A 2 2 0 0 1 22.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 38.5 107.5 L 49.5 107.5 A 2 2 0 0 1 51.5 109.5 L 51.5 115.5 A 0 0 0 0 1 51.5 115.5 L 36.5 115.5 A 0 0 0 0 1 36.5 115.5 L 36.5 109.5 A 2 2 0 0 1 38.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 55.5 102.5 L 65.5 102.5 A 2 2 0 0 1 67.5 104.5 L 67.5 115.5 A 0 0 0 0 1 67.5 115.5 L 53.5 115.5 A 0 0 0 0 1 53.5 115.5 L 53.5 104.5 A 2 2 0 0 1 55.5 102.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 71.5 86.5 L 82.5 86.5 A 2 2 0 0 1 84.5 88.5 L 84.5 115.5 A 0 0 0 0 1 84.5 115.5 L 69.5 115.5 A 0 0 0 0 1 69.5 115.5 L 69.5 88.5 A 2 2 0 0 1 71.5 86.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 88.5 38.5 L 98.5 38.5 A 2 2 0 0 1 100.5 40.5 L 100.5 115.5 A 0 0 0 0 1 100.5 115.5 L 86.5 115.5 A 0 0 0 0 1 86.5 115.5 L 86.5 40.5 A 2 2 0 0 1 88.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 104.5 54.5 L 115.5 54.5 A 2 2 0 0 1 117.5 56.5 L 117.5 115.5 A 0 0 0 0 1 117.5 115.5 L 102.5 115.5 A 0 0 0 0 1 102.5 115.5 L 102.5 56.5 A 2 2 0 0 1 104.5 54.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 120.5 73.5 L 131.5 73.5 A 2 2 0 0 1 133.5 75.5 L 133.5 115.5 A 0 0 0 0 1 133.5 115.5 L 118.5 115.5 A 0 0 0 0 1 118.5 115.5 L 118.5 75.5 A 2 2 0 0 1 120.5 73.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 137.5 86.5 L 148.5 86.5 A 2 2 0 0 1 150.5 88.5 L 150.5 115.5 A 0 0 0 0 1 150.5 115.5 L 135.5 115.5 A 0 0 0 0 1 135.5 115.5 L 135.5 88.5 A 2 2 0 0 1 137.5 86.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 153.5 95.5 L 164.5 95.5 A 2 2 0 0 1 166.5 97.5 L 166.5 115.5 A 0 0 0 0 1 166.5 115.5 L 151.5 115.5 A 0 0 0 0 1 151.5 115.5 L 151.5 97.5 A 2 2 0 0 1 153.5 95.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 170.5 100.5 L 180.5 100.5 A 2 2 0 0 1 182.5 102.5 L 182.5 115.5 A 0 0 0 0 1 182.5 115.5 L 168.5 115.5 A 0 0 0 0 1 168.5 115.5 L 168.5 102.5 A 2 2 0 0 1 170.5 100.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 186.5 104.5 L 197.5 104.5 A 2 2 0 0 1 199.5 106.5 L 199.5 115.5 A 0 0 0 0 1 199.5 115.5 L 184.5 115.5 A 0 0 0 0 1 184.5 115.5 L 184.5 106.5 A 2 2 0 0 1 186.5 104.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 203.5 107.5 L 213.5 107.5 A 2 2 0 0 1 215.5 109.5 L 215.5 115.5 A 0 0 0 0 1 215.5 115.5 L 201.5 115.5 A 0 0 0 0 1 201.5 115.5 L 201.5 109.5 A 2 2 0 0 1 203.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 219.5 107.5 L 230.5 107.5 A 2 2 0 0 1 232.5 109.5 L 232.5 115.5 A 0 0 0 0 1 232.5 115.5 L 217.5 115.5 A 0 0 0 0 1 217.5 115.5 L 217.5 109.5 A 2 2 0 0 1 219.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 235.5 107.5 L 246.5 107.5 A 2 2 0 0 1 248.5 109.5 L 248.5 115.5 A 0 0 0 0 1 248.5 115.5 L 233.5 115.5 A 0 0 0 0 1 233.5 115.5 L 233.5 109.5 A 2 2 0 0 1 235.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 252.5 107.5 L 263.5 107.5 A 2 2 0 0 1 265.5 109.5 L 265.5 115.5 A 0 0 0 0 1 265.5 115.5 L 250.5 115.5 A 0 0 0 0 1 250.5 115.5 L 250.5 109.5 A 2 2 0 0 1 252.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 268.5 107.5 L 279.5 107.5 A 2 2 0 0 1 281.5 109.5 L 281.5 115.5 A 0 0 0 0 1 281.5 115.5 L 266.5 115.5 A 0 0 0 0 1 266.5 115.5 L 266.5 109.5 A 2 2 0 0 1 268.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 285.5 107.5 L 295.5 107.5 A 2 2 0 0 1 297.5 109.5 L 297.5 115.5 A 0 0 0 0 1 297.5 115.5 L 283.5 115.5 A 0 0 0 0 1 283.5 115.5 L 283.5 109.5 A 2 2 0 0 1 285.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 301.5 107.5 L 312.5 107.5 A 2 2 0 0 1 314.5 109.5 L 314.5 115.5 A 0 0 0 0 1 314.5 115.5 L 299.5 115.5 A 0 0 0 0 1 299.5 115.5 L 299.5 109.5 A 2 2 0 0 1 301.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 161, 22, 1)" d="M 318.5 107.5 L 328.5 107.5 A 2 2 0 0 1 330.5 109.5 L 330.5 115.5 A 0 0 0 0 1 330.5 115.5 L 316.5 115.5 A 0 0 0 0 1 316.5 115.5 L 316.5 109.5 A 2 2 0 0 1 318.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point highcharts-point-select"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 334.5 107.5 L 345.5 107.5 A 2 2 0 0 1 347.5 109.5 L 347.5 115.5 A 0 0 0 0 1 347.5 115.5 L 332.5 115.5 A 0 0 0 0 1 332.5 115.5 L 332.5 109.5 A 2 2 0 0 1 334.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 350.5 107.5 L 361.5 107.5 A 2 2 0 0 1 363.5 109.5 L 363.5 115.5 A 0 0 0 0 1 363.5 115.5 L 348.5 115.5 A 0 0 0 0 1 348.5 115.5 L 348.5 109.5 A 2 2 0 0 1 350.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="rgba(255, 255, 255, 0.1)" d="M 367.5 107.5 L 378.5 107.5 A 2 2 0 0 1 380.5 109.5 L 380.5 115.5 A 0 0 0 0 1 380.5 115.5 L 365.5 115.5 A 0 0 0 0 1 365.5 115.5 L 365.5 109.5 A 2 2 0 0 1 367.5 107.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path></g><g class="highcharts-markers highcharts-series-0 highcharts-column-series" data-z-index="0.1" opacity="1" transform="translate(0,0) scale(1 1)" clip-path="none"></g><g class="highcharts-series highcharts-series-1 highcharts-column-series highcharts-tracker" data-z-index="0.1" opacity="1" transform="translate(0,0) scale(1 1)" clip-path="url(#highcharts-w04asvk-193-)"><path fill="transparent" d="M 5.5 38.5 L 17.5 38.5 A 2 2 0 0 1 19.5 40.5 L 19.5 115.5 A 0 0 0 0 1 19.5 115.5 L 3.5 115.5 A 0 0 0 0 1 3.5 115.5 L 3.5 40.5 A 2 2 0 0 1 5.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 21.5 38.5 L 33.5 38.5 A 2 2 0 0 1 35.5 40.5 L 35.5 115.5 A 0 0 0 0 1 35.5 115.5 L 19.5 115.5 A 0 0 0 0 1 19.5 115.5 L 19.5 40.5 A 2 2 0 0 1 21.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 37.5 38.5 L 50.5 38.5 A 2 2 0 0 1 52.5 40.5 L 52.5 115.5 A 0 0 0 0 1 52.5 115.5 L 35.5 115.5 A 0 0 0 0 1 35.5 115.5 L 35.5 40.5 A 2 2 0 0 1 37.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 54.5 38.5 L 66.5 38.5 A 2 2 0 0 1 68.5 40.5 L 68.5 115.5 A 0 0 0 0 1 68.5 115.5 L 52.5 115.5 A 0 0 0 0 1 52.5 115.5 L 52.5 40.5 A 2 2 0 0 1 54.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 70.5 38.5 L 83.5 38.5 A 2 2 0 0 1 85.5 40.5 L 85.5 115.5 A 0 0 0 0 1 85.5 115.5 L 68.5 115.5 A 0 0 0 0 1 68.5 115.5 L 68.5 40.5 A 2 2 0 0 1 70.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 87.5 38.5 L 99.5 38.5 A 2 2 0 0 1 101.5 40.5 L 101.5 115.5 A 0 0 0 0 1 101.5 115.5 L 85.5 115.5 A 0 0 0 0 1 85.5 115.5 L 85.5 40.5 A 2 2 0 0 1 87.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 103.5 38.5 L 116.5 38.5 A 2 2 0 0 1 118.5 40.5 L 118.5 115.5 A 0 0 0 0 1 118.5 115.5 L 101.5 115.5 A 0 0 0 0 1 101.5 115.5 L 101.5 40.5 A 2 2 0 0 1 103.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 120.5 38.5 L 132.5 38.5 A 2 2 0 0 1 134.5 40.5 L 134.5 115.5 A 0 0 0 0 1 134.5 115.5 L 118.5 115.5 A 0 0 0 0 1 118.5 115.5 L 118.5 40.5 A 2 2 0 0 1 120.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 136.5 38.5 L 148.5 38.5 A 2 2 0 0 1 150.5 40.5 L 150.5 115.5 A 0 0 0 0 1 150.5 115.5 L 134.5 115.5 A 0 0 0 0 1 134.5 115.5 L 134.5 40.5 A 2 2 0 0 1 136.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 152.5 38.5 L 165.5 38.5 A 2 2 0 0 1 167.5 40.5 L 167.5 115.5 A 0 0 0 0 1 167.5 115.5 L 150.5 115.5 A 0 0 0 0 1 150.5 115.5 L 150.5 40.5 A 2 2 0 0 1 152.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 169.5 38.5 L 181.5 38.5 A 2 2 0 0 1 183.5 40.5 L 183.5 115.5 A 0 0 0 0 1 183.5 115.5 L 167.5 115.5 A 0 0 0 0 1 167.5 115.5 L 167.5 40.5 A 2 2 0 0 1 169.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 185.5 38.5 L 198.5 38.5 A 2 2 0 0 1 200.5 40.5 L 200.5 115.5 A 0 0 0 0 1 200.5 115.5 L 183.5 115.5 A 0 0 0 0 1 183.5 115.5 L 183.5 40.5 A 2 2 0 0 1 185.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 202.5 38.5 L 214.5 38.5 A 2 2 0 0 1 216.5 40.5 L 216.5 115.5 A 0 0 0 0 1 216.5 115.5 L 200.5 115.5 A 0 0 0 0 1 200.5 115.5 L 200.5 40.5 A 2 2 0 0 1 202.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 218.5 38.5 L 231.5 38.5 A 2 2 0 0 1 233.5 40.5 L 233.5 115.5 A 0 0 0 0 1 233.5 115.5 L 216.5 115.5 A 0 0 0 0 1 216.5 115.5 L 216.5 40.5 A 2 2 0 0 1 218.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 235.5 38.5 L 247.5 38.5 A 2 2 0 0 1 249.5 40.5 L 249.5 115.5 A 0 0 0 0 1 249.5 115.5 L 233.5 115.5 A 0 0 0 0 1 233.5 115.5 L 233.5 40.5 A 2 2 0 0 1 235.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 251.5 38.5 L 263.5 38.5 A 2 2 0 0 1 265.5 40.5 L 265.5 115.5 A 0 0 0 0 1 265.5 115.5 L 249.5 115.5 A 0 0 0 0 1 249.5 115.5 L 249.5 40.5 A 2 2 0 0 1 251.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 267.5 38.5 L 280.5 38.5 A 2 2 0 0 1 282.5 40.5 L 282.5 115.5 A 0 0 0 0 1 282.5 115.5 L 265.5 115.5 A 0 0 0 0 1 265.5 115.5 L 265.5 40.5 A 2 2 0 0 1 267.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 284.5 38.5 L 296.5 38.5 A 2 2 0 0 1 298.5 40.5 L 298.5 115.5 A 0 0 0 0 1 298.5 115.5 L 282.5 115.5 A 0 0 0 0 1 282.5 115.5 L 282.5 40.5 A 2 2 0 0 1 284.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 300.5 38.5 L 313.5 38.5 A 2 2 0 0 1 315.5 40.5 L 315.5 115.5 A 0 0 0 0 1 315.5 115.5 L 298.5 115.5 A 0 0 0 0 1 298.5 115.5 L 298.5 40.5 A 2 2 0 0 1 300.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 317.5 38.5 L 329.5 38.5 A 2 2 0 0 1 331.5 40.5 L 331.5 115.5 A 0 0 0 0 1 331.5 115.5 L 315.5 115.5 A 0 0 0 0 1 315.5 115.5 L 315.5 40.5 A 2 2 0 0 1 317.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 333.5 38.5 L 346.5 38.5 A 2 2 0 0 1 348.5 40.5 L 348.5 115.5 A 0 0 0 0 1 348.5 115.5 L 331.5 115.5 A 0 0 0 0 1 331.5 115.5 L 331.5 40.5 A 2 2 0 0 1 333.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 350.5 38.5 L 362.5 38.5 A 2 2 0 0 1 364.5 40.5 L 364.5 115.5 A 0 0 0 0 1 364.5 115.5 L 348.5 115.5 A 0 0 0 0 1 348.5 115.5 L 348.5 40.5 A 2 2 0 0 1 350.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path><path fill="transparent" d="M 366.5 38.5 L 378.5 38.5 A 2 2 0 0 1 380.5 40.5 L 380.5 115.5 A 0 0 0 0 1 380.5 115.5 L 364.5 115.5 A 0 0 0 0 1 364.5 115.5 L 364.5 40.5 A 2 2 0 0 1 366.5 38.5 Z" stroke="#282828" stroke-width="1" opacity="1" filter="none" class="highcharts-point"></path></g><g class="highcharts-markers highcharts-series-1 highcharts-column-series" data-z-index="0.1" opacity="1" transform="translate(0,0) scale(1 1)" clip-path="none"></g></g><text x="193" text-anchor="middle" class="highcharts-title" data-z-index="4" style="font-size: 1.2em; color: rgb(51, 51, 51); font-weight: bold; display: none; fill: rgb(51, 51, 51);" y="25"></text><text x="193" text-anchor="middle" class="highcharts-subtitle" data-z-index="4" style="color: rgb(102, 102, 102); font-size: 0.8em; fill: rgb(102, 102, 102);" y="24"></text><text x="10" text-anchor="start" class="highcharts-caption" data-z-index="4" style="color: rgb(102, 102, 102); font-size: 0.8em; fill: rgb(102, 102, 102);" y="112"></text><g class="highcharts-legend highcharts-no-tooltip" data-z-index="7" visibility="hidden"><rect fill="none" class="highcharts-legend-box" rx="0" ry="0" stroke="#999999" stroke-width="0" filter="none" x="0" y="0" width="8" height="8"></rect><g data-z-index="1"><g></g></g></g><g class="highcharts-control-points" data-z-index="99" clip-path="url(#highcharts-w04asvk-217-)"></g></svg></div></div></div></div></div></div>
'''
    return top_chart_n_stuff_const


import random

import random

import random

import random

import random

import random

const_365_days = '''
()=>{

const el = document.getElementsByClassName(
            'bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg h-[180px] w-full flex-1'
        )[0];

        if (el) {
            el.outerHTML = `<div class="bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg h-[180px] w-full flex-1"><div class="p-4"><div><div class="flex items-start justify-between"><div><div class="text-label-3 dark:text-dark-label-3 text-xs">Badges</div><div class="text-label-1 dark:text-dark-label-1 mt-1.5 text-2xl leading-[18px]">45</div></div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="h-[24px] w-[24px] text-label-3 dark:text-dark-label-3 cursor-pointer"><path fill-rule="evenodd" d="M18.586 13H3a1 1 0 110-2h15.586L12 4.414A1 1 0 0113.414 3l8.293 8.293a.997.997 0 01-.003 1.417L13.414 21A1 1 0 0112 19.586L18.586 13z" clip-rule="evenodd"></path></svg></div><div class="flex items-center justify-center"><div class="mr-[28px] h-[56px] w-[56px]"><img alt="500 Days Badge" class="h-full w-full cursor-pointer object-contain" data-state="closed" src="https://assets.leetcode.com/static_assets/marketing/lg500.png"></div><div class="mr-[28px] h-[72px] w-[72px]"><img alt="Guardian" class="h-full w-full cursor-pointer object-contain" data-state="closed" src="/static/images/badges/guardian.png"></div><div class="h-[56px] w-[56px]"><img alt="365 Days Badge" class="h-full w-full cursor-pointer object-contain" data-state="closed" src="https://assets.leetcode.com/static_assets/marketing/lg365.png"></div></div><div class="text-label-3 dark:text-dark-label-3 text-xs">Most Recent Badge</div><div class="text-label-1 dark:text-dark-label-1 text-base">Guardian</div></div></div></div>`
}

}
'''


async def get_bottom_table_n_stuff():
    # List of LeetCode-style problem names (no repetition)
    problem_names = [
        "Stone Game IX",
        "Longest Subsequence With Non-Zero Bitwise XOR",
        "Maximum Length Substring With Two Occurrences",
        "Longest Substring of One Repeating Character",
        "Length of Longest Subarray With at Most K Frequency",
        "Smallest Missing Integer Greater Than Sequential Prefix Sum",
        "Stone Game IV",
        "Stone Game II",
        "Find the Lexicographically Smallest Valid Sequence",
        "Smallest Divisible Digit Product II",
        "Smallest Divisible Digit Product I",
        "Remove Methods From Project",
        "Find Missing Elements",
        "Stone Game",
        "Stone Game III",
        "Maximum Subarray Sum With One Deletion",
        "Longest Palindrome After Substring Concatenation",
        "Minimum Operations to Make Array Equal",
        "Maximum Product of Splitted Binary Tree",
        "Number of Ways to Reorder Array to Get Same BST",
        "Maximum Performance of a Team",
        "Minimum Time to Complete Trips",
        "Maximum Number of Events That Can Be Attended II",
        "Minimum Number of Operations to Make Array Continuous",
        "Maximum Subsequence Score",
        "Minimum Cost to Connect Two Groups of Points",
        "Maximum Number of Ways to Partition an Array",
        "Minimum Operations to Make the Array Increasing",
        "Maximum Number of Groups Getting Fresh Donuts",
        "Minimum Cost to Make Array Equalindromic"
    ]

    hours = random.sample(range(1, 24), 15)
    hours.sort()

    time_strings = []
    for i in hours:
        if i == 1:
            time_strings.append("1 hour ago")
        else:
            time_strings.append(f"{i} hours ago")

    random.shuffle(problem_names)
    selected_problems = problem_names[:15]

    html_stuff = []

    # Header
    header = '''<div class="bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg px-4 pb-4 pt-4"><div class="space-y-[18px]"><div class="text-label-2 dark:text-dark-label-2 flex w-full items-center overflow-y-hidden"><div class="cursor-pointer"><div class="text-label-1 dark:text-dark-label-1 bg-fill-3 dark:bg-dark-fill-3 flex items-center rounded-[5px] px-5 py-[10px] font-medium lc-md:space-x-2 hover:text-label-1 dark:hover:text-dark-label-1"><span class="hidden text-2xl lc-md:inline"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M20.995 4.824A3 3 0 0018 2H6l-.176.005A3 3 0 003 5v14l.005.176A3 3 0 006 22h12l.176-.005A3 3 0 0021 19V5l-.005-.176zM6 4h12l.117.007A1 1 0 0119 5v14l-.007.117A1 1 0 0118 20H6l-.117-.007A1 1 0 015 19V5l.007-.117A1 1 0 016 4zm5.718 9.304a1 1 0 01.063 1.321l-.085.093-2.062 2a1 1 0 01-1.3.08l-.093-.08-.937-.91A1 1 0 018.6 14.292l.095.082.241.234 1.367-1.325a1 1 0 011.414.022zM17 15a1 1 0 00-1-1h-2l-.117.007A1 1 0 0014 16h2l.117-.007A1 1 0 0017 15zm-5.282-7.696a1 1 0 01.063 1.321l-.085.093-2.062 2a1 1 0 01-1.3.08l-.093-.08-.937-.91A1 1 0 018.6 8.292l.095.082.241.234 1.367-1.325a1 1 0 011.414.022zM17 9a1 1 0 00-1-1h-2l-.117.007A1 1 0 0014 10h2l.117-.007A1 1 0 0017 9z" clip-rule="evenodd"></path></svg></span><span class="whitespace-nowrap">Recent AC</span></div></div><div class="cursor-pointer"><div class="flex items-center rounded-[5px] px-5 py-[10px] font-medium lc-md:space-x-2 hover:text-label-1 dark:hover:text-dark-label-1"><span class="hidden text-2xl lc-md:inline"><div class="relative text-[20px] leading-[normal] p-0.5 before:block before:h-5 before:w-5"><svg aria-hidden="true" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" height="1em" width="0.75em" class="svg-inline--fa fa-file-lines absolute h-[1em] -translate-x-1/2 -translate-y-1/2 align-[-0.125em] left-1/2 top-1/2"><path fill="currentColor" d="M64 464c-8.8 0-16-7.2-16-16V64c0-8.8 7.2-16 16-16H224v80c0 17.7 14.3 32 32 32h80V448c0 8.8-7.2 16-16 16H64zM64 0C28.7 0 0 28.7 0 64V448c0 35.3 28.7 64 64 64H320c35.3 0 64-28.7 64-64V154.5c0-17-6.7-33.3-18.7-45.3L274.7 18.7C262.7 6.7 246.5 0 229.5 0H64zm56 256c-13.3 0-24 10.7-24 24s10.7 24 24 24H264c13.3 0 24-10.7 24-24s-10.7-24-24-24H120zm0 96c-13.3 0-24 10.7-24 24s10.7 24 24 24H264c13.3 0 24-10.7 24-24s-10.7-24-24-24H120z"></path></svg></div></span><span class="whitespace-nowrap">List</span></div></div><div class="cursor-pointer"><div class="flex items-center rounded-[5px] px-5 py-[10px] font-medium lc-md:space-x-2 hover:text-label-1 dark:hover:text-dark-label-1"><span class="hidden text-2xl lc-md:inline"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M20.995 4.824A3 3 0 0018 2H6l-.176.005A3 3 0 003 5v14l.005.176A3 3 0 006 22h12l.176-.005A3 3 0 0021 19V5l-.005-.176zM6 4h12l.117.007A1 1 0 0119 5v14l-.007.117A1 1 0 0118 20H6l-.117-.007A1 1 0 015 19V5l.007-.117A1 1 0 016 4z" clip-rule="evenodd"></path><path fill-rule="evenodd" d="M10.763 12.827l-1.06-1.06a1 1 0 00-1.415 1.414l1.415 1.414a1.5 1.5 0 002.12 0l3.889-3.888a1 1 0 00-1.415-1.414l-3.534 3.534z" clip-rule="evenodd"></path></svg></span><span class="whitespace-nowrap">Solutions</span></div></div><div class="cursor-pointer"><div class="flex items-center rounded-[5px] px-5 py-[10px] font-medium lc-md:space-x-2 hover:text-label-1 dark:hover:text-dark-label-1"><span class="hidden text-2xl lc-md:inline"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M2 11.001a9.001 9.001 0 014.974-8.047A8.876 8.876 0 0110.998 2h.535c.018 0 .037 0 .055.002 3.934.218 7.204 3.02 8.15 6.753a1 1 0 01-1.94.49c-.734-2.9-3.27-5.065-6.294-5.245h-.51a6.876 6.876 0 00-3.12.74l-.004.002A7.001 7.001 0 004 11.003v.002a6.873 6.873 0 00.738 3.117c.206.407.271.871.185 1.32l-.387 2.022 2.022-.387c.448-.086.912-.021 1.32.185.44.222.9.395 1.373.518a1 1 0 11-.502 1.936 8.865 8.865 0 01-1.773-.669.067.067 0 00-.042-.006l-3.47.665a1 1 0 01-1.17-1.17l.665-3.47a.067.067 0 00-.006-.043A8.873 8.873 0 012 11.001zM17.004 20h-.005a3 3 0 01-2.68-1.658l-.004-.007A2.936 2.936 0 0114 17.004v-.206a2.995 2.995 0 012.773-2.797l.233-.001c.46-.001.917.107 1.33.315l.007.004A3 3 0 0120 17v.005c.001.425-.09.845-.268 1.232l-.133.29a1 1 0 00-.074.606l.093.485-.484-.093a1 1 0 00-.606.073l-.29.134a2.937 2.937 0 01-1.234.268zm-.296-8A4.995 4.995 0 0012 16.738v.262c-.002.777.18 1.543.53 2.237a5 5 0 006.542 2.313l2.303.441c.365.07.686-.25.616-.615l-.441-2.303a5 5 0 00-2.312-6.541A4.937 4.937 0 0017 12h-.292z" clip-rule="evenodd"></path></svg></span><span class="whitespace-nowrap">Discuss</span></div></div><div class="ml-auto flex items-center overflow-auto whitespace-nowrap hidden" style="overflow-x: hidden;"><div class="group ml-4 inline-block items-center space-x-4"><div class="text-label-1 dark:text-dark-label-1 flex cursor-pointer items-center space-x-2"><span class="text-base group-hover:text-gray-8 dark:group-hover:text-dark-gray-8 text-gray-8 dark:text-dark-gray-8"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 100-16 8 8 0 000 16zm1-13.4v4.782l3.047 1.524a1 1 0 11-.894 1.788l-3.6-1.8A1 1 0 0111 12V6.6a1 1 0 112 0z" clip-rule="evenodd"></path></svg></span><span class="text-xs group-hover:text-label-1 dark:group-hover:text-dark-label-1 text-label-1 dark:text-dark-label-1">Most Recent</span></div></div><div class="w-px ml-4 inline-block h-3 bg-gray-3 dark:bg-dark-gray-3"></div><div class="group ml-4 inline-block items-center space-x-4"><div class="flex cursor-pointer items-center space-x-2"><span class="text-base group-hover:text-gray-8 dark:group-hover:text-dark-gray-8 text-gray-6 dark:text-dark-gray-6"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" width="1em" height="1em" fill="currentColor"><path fill-rule="evenodd" d="M7.19 1.564a.75.75 0 01.729.069c2.137 1.475 3.373 3.558 3.981 5.002l.641-.663a.75.75 0 011.17.115c1.633 2.536 1.659 5.537.391 7.725-1.322 2.282-3.915 2.688-5.119 2.688-1.177 0-3.679-.203-5.12-2.688-.623-1.076-.951-2.29-.842-3.528.109-1.245.656-2.463 1.697-3.54.646-.67 1.129-1.592 1.468-2.492.337-.895.51-1.709.564-2.105a.75.75 0 01.44-.583zm.784 2.023c-.1.368-.226.773-.385 1.193-.375.997-.947 2.13-1.792 3.005-.821.851-1.205 1.754-1.282 2.63-.078.884.153 1.792.647 2.645C6.176 14.81 7.925 15 8.983 15c1.03 0 2.909-.366 3.822-1.94.839-1.449.97-3.446.11-5.315l-.785.812a.75.75 0 01-1.268-.345c-.192-.794-1.04-2.948-2.888-4.625z" clip-rule="evenodd"></path></svg></span><span class="text-xs group-hover:text-label-1 dark:group-hover:text-dark-label-1 text-label-3 dark:text-dark-label-3">Most Votes</span></div></div></div></div><div class="flex flex-col">'''
    html_stuff.append(header)

    for i in range(15):
        problem_name = selected_problems[i]
        time_str = time_strings[i]
        if i % 2 == 0:
            bg_class = "bg-fill-4 dark:bg-dark-fill-4"
        else:
            bg_class = ""
        row_html = f'''<a class="flex h-[56px] items-center rounded px-4 {bg_class}" target="_blank" href="/submissions/detail/{random.randint(2000000000, 2200000000)}/"><div data-title="{problem_name}" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">{problem_name}</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">{time_str}</span></div></a>'''
        html_stuff.append(row_html)

    footer = '''</div></div></div>'''
    html_stuff.append(footer)

    return ''.join(html_stuff)


async def get_image_dict(starting_month_number):
    currnet_year = datetime.now().year
    past_year = currnet_year - 1
    data = {}
    for i in range(starting_month_number, 1 - 1, -1):
        data[i] = f'https://leetcode.com/static/images/badges/dcc-{past_year}-{i}.png'

    for i in range(starting_month_number, 12 + 1):
        data[i] = f'https://leetcode.com/static/images/badges/dcc-{currnet_year}-{i}.png'

    return data


async def create_all_labels_list_to_append(starting_month_number, month_name):
    starting_month_number = int(starting_month_number)
    # data=get_image_dict(starting_month_number)
    currnet_year = datetime.now().year
    past_year = currnet_year - 1
    list_ = []
    count = 0
    # call that recalculating sapaicng of x fuction here
    first_ele = f'''<text x="{spacesof_x[count]}" y="97.14" font-size="14px" fill="#AFB4BD" class="font-xs">{month_name}</text>'''
    list_.append(first_ele)
    count += 1
    for i in range(starting_month_number + 1, 12 + 1):
        try:
            str_ = f'''<image xlink:href="/static/images/badges/dcc-{past_year}-{i}.png" x="{spacesof_x[count]}" y="82.64" width="22" height="22"></image>'''
            count += 1
            list_.append(str_)
        except Exception as e:
            print(f'error 1 : {e}')
    for i in range(1, starting_month_number):
        try:
            str_ = f'''<image xlink:href="/static/images/badges/dcc-{currnet_year}-{i}.png" x="{spacesof_x[count]}" y="82.64" width="22" height="22"></image>'''
            count += 1
            list_.append(str_)
        except Exception as e:
            print(f'eroor 2 : {e}')
    print('count=>', count)
    last_ele = f'''<text x="{spacesof_x[count]}" y="97.14" font-size="14px" fill="#AFB4BD" class="font-xs">{month_name}</text>'''
    list_.append(last_ele)
    return list_


pfp_url = 'https://leetcode.com/u/d1zpNU7oGC'


import asyncio
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


async def safe_goto(page, url, timeout=30000, max_retries=3):
    wait_strategies = ["networkidle", "load", "domcontentloaded"]

    for trys in range(1, max_retries + 1):
        strategy = wait_strategies[min(trys - 1, len(wait_strategies) - 1)]
        try:
            print(f"attempt {trys}/{max_retries} -> "
                  f"goto(wait_until='{strategy}')")
            await page.goto(url, wait_until=strategy, timeout=timeout)
            print(f"page loaded successfully on attempt {trys}.")
            return True
        except PlaywrightTimeoutError:
            print(f"timeout on attempt {trys} using '{strategy}'.")
        except Exception as e:
            print(f"navigation error on attempt {trys} => {e}")

        if trys < max_retries:
            await asyncio.sleep(2)

    print(f"all {max_retries} attempts failed for {url}")
    return False

app = FastAPI()


@app.get("/screenshot")
async def screenshot(pfp_url:str, change_:int):
    async def main_():
        async with async_playwright() as p:
            yield json.dumps({
                "status": "starting browser",
                "pfp_url": pfp_url,
                "change_": change_
            }) + "\n"
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--disable-dev-shm-usage",
                    "--no-sandbox",
                ]
            )
            yield json.dumps({
                "status": "launching browser"
            }) + "\n"
            context = await browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/128.0.0.0 Safari/537.36"
                ),
                viewport={"width": 1920, "height": 1080},
                locale="en-US",
                timezone_id="Asia/Kolkata",
            )
            yield json.dumps({
                "status": "creating page"
            }) + "\n"
            await context.add_init_script(
                "Object.defineProperty(navigator,'webdriver',{get: ()=>undefined})"
            )

            await context.add_init_script(
                "localStorage.setItem('lc-theme','dark');"
                "document.documentElement.classList.remove('light');"
                "document.documentElement.classList.add('dark');"
                "document.documentElement.style.colorScheme='dark';"
            )

            page = await context.new_page()
            print("page created successfully")

            # -----------------------------
            # GOTO WITH RETRIES
            # -----------------------------

            wait_strategies = [
                "networkidle",
                "load",
                "domcontentloaded"
            ]

            max_retries = 3
            timeout = 30000
            loaded = False

            for trys in range(1, max_retries + 1):

                strategy = wait_strategies[
                    min(trys - 1, len(wait_strategies) - 1)
                ]

                try:
                    print(
                        f"attempt {trys}/{max_retries} -> "
                        f"goto(wait_until='{strategy}')"
                    )

                    await page.goto(
                        pfp_url,
                        wait_until=strategy,
                        timeout=timeout
                    )

                    print(
                        f"page loaded successfully on attempt {trys}."
                    )

                    loaded = True
                    break

                except PlaywrightTimeoutError:
                    print(
                        f"timeout on attempt {trys} "
                        f"using '{strategy}'."
                    )

                except Exception as e:
                    print(
                        f"navigation error on attempt {trys} => {e}"
                    )

                if trys < max_retries:
                    await asyncio.sleep(2)

            if not loaded:
                print(f"all {max_retries} attempts failed for {pfp_url}")
                yield json.dumps({
                    "status":f"all {max_retries} attempts failed for {pfp_url}"
                }) + "\n"
            if not loaded:
                print(f"giving up on {pfp_url} after retries not crashing")
                await browser.close()

            is_dark = await page.evaluate(
                "document.documentElement.classList.contains('dark')"
            )
            print(f"dark mode applied : {is_dark}")
            yield json.dumps({
                "status": "dark mode applied successfully"
            }) + "\n"
            await page.wait_for_timeout(3000)
            await page.evaluate(const_365_days)
            print("title:", await page.title())
            print("url:", page.url)
            yield json.dumps({
                "status": "repopulating submits and green lush"
            }) + "\n"
            await page.evaluate('''
                ()=>{   let a=document.getElementsByClassName('hidden h-auto w-full flex-1 items-center justify-center lc-md:flex')[0].children[0].children;
                const result = [];
            let easy=0;let medium=0;let hard=0;

            const question_schema={0:{questions:0,type:null},1:{questions:4,type:"easy"},2:{questions:3,type:"medium"},3:{questions:2,type:"hard"},4:{questions:5,type:"easy"}};




            for (const i of a) {
                const className = i.getAttribute("class");

                if (className && className.includes("month")) {
                    result.push(i);
                }
            }

            console.log(result);
            let month=result[1];


            for (const i of month.childNodes){
                console.log('good');
                for (const d of i.childNodes){
                    if (d.className['animVal']=='cursor-pointer'){
                        console.log('day');
                    }
                }
            }
            // fill="var(--fill-tertiary)" // black
            // fill="var(--green-80)" // lightest green
            // fill="var(--green-60)" // second less lightest green
            // fill="var(--green-40)" // third less lightest green
            // fill="var(--green-20)" // dark green

            const colors = ["var(--fill-tertiary)","var(--green-80)","var(--green-60)","var(--green-40)","var(--green-20)"];
            // for (const i of month.childNodes) {
            //     console.log('good');

            //     for (const d of i.childNodes) {

            //         if (
            //             d.tagName === 'rect' &&
            //             d.className['animVal'] === 'cursor-pointer'
            //         ) {

            //             console.log('day');

            //             d.removeAttribute('fill');
            //             let idx=Math.floor(Math.random() * 4);
            //             if (idx==0){
            //             idx=Math.floor(Math.random() * 4);
            //             }

            //             d.setAttribute('fill',colors[idx]);
            //             if (question_schema[idx].type === "easy") {
            //     easy += question_schema[idx].questions;
            // }

            // else if (question_schema[idx].type === "medium") {
            //     medium += question_schema[idx].questions;
            // }

            // else if (question_schema[idx].type === "hard") {
            //     hard += question_schema[idx].questions;
            // }
            //         }
            //     }




            // }



            let streak_dat=[];
            let question_dat=[];
            for (const i of a) {
                const className = i.getAttribute("class");

                if (className && className.includes("month")) {
                    result.push(i);
                    for (const m of i.childNodes) {
                console.log('good');

                for (const d of m.childNodes) {

                    if (
                        d.tagName === 'rect' &&
                        d.className['animVal'] === 'cursor-pointer'
                    ) {

                        console.log('day');

                        d.removeAttribute('fill');
                                    let idx=Math.floor(Math.random() * 4);
                        if (idx==0){
                        idx=Math.floor(Math.random() * 4);
                        }
                        if (idx==0){
                            streak_dat.push(0);
                        }
                        else if (idx!=0){
                            streak_dat.push(1);
                        }
                        question_dat.push(question_schema[idx].questions);

                        d.setAttribute('fill',colors[idx]);
                        if (question_schema[idx].type === "easy") {
                easy+=question_schema[idx].questions;
            }

            else if (question_schema[idx].type === "medium") {
                medium+=question_schema[idx].questions;
            }

            else if (question_schema[idx].type === "hard") {
                hard+=question_schema[idx].questions;
            }
                        d.setAttribute('fill',colors[idx]);
                    }
                }
            }

                }
            }

            document.getElementsByClassName('text-xs font-medium text-sd-foreground')[0].innerText=`${easy}/943`;

            document.getElementsByClassName('text-xs font-medium text-sd-foreground')[1].innerText=`${medium}/2054`;

            document.getElementsByClassName('text-xs font-medium text-sd-foreground')[2].innerText=`${hard}/931`;
            console.log(question_dat);

            // calculate max streak
            let max=0;
            let current=0;

            for (const i of streak_dat){

                if (i===1){
                    current++;
                    max=Math.max(max,current);
                }else{
                    current=0;
                }

            }

            console.log(max);


            let t_active_day=0;
            for (const i of streak_dat){
                if (i==1) t_active_day+=1;
            }

            console.log(t_active_day);
            let subm_count=Math.round(t_active_day*5.5);
            console.log(subm_count);


            document.getElementsByClassName('font-medium text-label-2 dark:text-dark-label-2')[0].innerText=`${t_active_day}`;

            document.getElementsByClassName('font-medium text-label-2 dark:text-dark-label-2')[1].innerText=`${max}`;
            document.getElementsByClassName('mr-[5px] text-base font-medium lc-md:text-xl')[0].innerText=`${subm_count}`;

            const functions = [
                () => {
                    let progress = easy /943;

                    let x=45*progress;
                    let y =264+(219-264)*progress;

                    return `${x.toFixed(2)},${y.toFixed(2)}`;
                },

                () => {
                    let progress = medium / 2054;

                    let x = 98 * progress;
                    let y = 264 + (166 - 264) * progress;

                    return `${x.toFixed(2)},${y.toFixed(2)}`;
                },

                () => {
                    let progress = hard / 931;

                    let x = 43 * progress;
                    let y = 264 + (220 - 264) * progress;

                    return `${x.toFixed(2)},${y.toFixed(2)}`;
                }
            ];

            console.log(functions[0]());
            console.log(functions[1]());
            console.log(functions[2]());


            let count_=0;
            let all_3=document.getElementById('bar-mask').parentElement.nextSibling.children
            ;
            for (const i of all_3) {
                let a=i.children[1];

                a.style.strokeDasharray=functions[count_]();
                count_+=1;
                console.log(a);
            }


            // total solved
            document.getElementsByClassName('pointer-events-none absolute flex -translate-x-1/2 -translate-y-1/2 flex-col items-center gap-0.5 text-sm text-sd-foreground transition-opacity duration-200 left-1/2 top-1/2 opacity-100 delay-200')[0].childNodes[0].childNodes[0].innerText=`${easy+medium+hard}`

            // rank 
            document.getElementsByClassName('ttext-label-1 dark:text-dark-label-1 font-medium')[0].innerText=(Math.floor(Math.random()*(40000-30000+1))+30000).toLocaleString();


            // community 0-3
            // document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[3].parentNode.childNodes

            // document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0].parentNode.childNodes[0].children[2].innerText='250' // bold one
            // document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0].parentNode.childNodes[1].children[1].innerText='50'  // non bold one
            let _a1=(Math.random()*(40-15)+15).toFixed(1)+"K";
            let _a2 = Math.floor(Math.random() * (100 - 50 + 1)) + 50;

            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0]
                .parentNode.childNodes[1].children[1].innerHTML=`<span><span class="text-blue-s dark:text-dark-blue-s">+${_a2}</span></span>`;
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0].parentNode.childNodes[0].children[2].innerText=`${_a1}`;



            function solutionCount(a){

            let total=0;
            let week=0;

            for(let i=0;i<a.length;i++){

            if(a[i]>0) total++;

            if(i>=a.length-7 && a[i]>0) week++;

            }

            return [Math.floor(total/1),Math.floor(week/1)];

            }

            let [solutions,last_week]=solutionCount(question_dat);

            console.log(solutions);
            console.log(last_week);
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[1].parentNode.childNodes[0].children[2].innerText=`${solutions}`;
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[1].parentNode.childNodes[1].children[1].innerText=`${Math.floor(last_week)}`;


            let _b1=Math.floor(Math.random()*10)+300;
            let _b2=Math.floor(Math.random()*_b1);
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[3].parentNode.childNodes[0].children[2].innerText=`${_b1}`;
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[3].parentNode.childNodes[1].children[1].innerText=`${_b2}`;


            let _c1=Math.floor(Math.random()*6)+1;
            let _c2=Math.floor(Math.random()*_c1);
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[2].parentNode.childNodes[0].children[2].innerText=`${_c1}`;
            document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[2].parentNode.childNodes[1].children[1].innerText=`${_c2}`;



            let count_lang=document.getElementsByClassName('flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1');
            //if (count_lange == 0) {

            let oldDiv1=document.getElementsByClassName('mt-3 flex items-center justify-center space-y-4 text-xs text-label-4 dark:text-dark-label-4')[0];
            if(oldDiv1)oldDiv1.remove();

            let oldDiv2=document.getElementsByClassName('mt-4 flex flex-col space-y-3')[0];
            if(oldDiv2)oldDiv2.remove();

            let target=document.getElementsByClassName('text-base font-medium leading-6')[1];

            if(target){

            let newDiv=document.createElement("div");

            newDiv.innerHTML=`<div class="mt-4 flex flex-col space-y-3">

            <div class="flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1"><div class="text-xs"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate">Java</span></div><div class="flex"><span class="text-xs font-medium text-label-1 dark:text-dark-label-1">${Math.round(641*(Math.random()*0.5+1))}</span>&nbsp;<span class="text-label-3 dark:text-dark-label-3">problems solved</span></div></div>

            <div class="flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1"><div class="text-xs"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate">JavaScript</span></div><div class="flex"><span class="text-xs font-medium text-label-1 dark:text-dark-label-1">${Math.round(41*(Math.random()*0.5+1))}</span>&nbsp;<span class="text-label-3 dark:text-dark-label-3">problems solved</span></div></div>

            <div class="flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1"><div class="text-xs"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate">MySQL</span></div><div class="flex"><span class="text-xs font-medium text-label-1 dark:text-dark-label-1">${Math.round(39*(Math.random()*0.5+1))}</span>&nbsp;<span class="text-label-3 dark:text-dark-label-3">problems solved</span></div></div>

            <div class="flex items-center justify-center text-xs text-label-3 dark:text-dark-label-3"><span class="cursor-pointer">Show more</span></div>

            </div>`;

            target.insertAdjacentElement("afterend",newDiv.firstElementChild);
            }



            let tar=document.getElementsByClassName('text-base font-medium leading-6')[2];

            if(tar){

            if(tar.nextElementSibling)tar.nextElementSibling.remove();

            let newDiv=document.createElement("div");

            newDiv.innerHTML=`<div class="mt-4 flex flex-col space-y-4"><div><div class="flex items-center text-xs"><span class="mr-1.5 flex"><span class="inline-block h-1 w-1 rounded-full bg-red-s dark:bg-dark-red-s"></span></span><span class="font-medium">Advanced</span></div><div class="mt-3 flex flex-wrap"><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/dynamic-programming/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Dynamic Programming</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x62</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/backtracking/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Backtracking</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x27</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/union-find/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Union-Find</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x17</span></div></div><div class="flex items-center justify-center text-xs text-label-3 dark:text-dark-label-3"><span class="cursor-pointer">Show more</span></div></div><div><div class="flex items-center text-xs"><span class="mr-1.5 flex"><span class="inline-block h-1 w-1 rounded-full bg-yellow dark:bg-dark-yellow"></span></span><span class="font-medium">Intermediate</span></div><div class="mt-3 flex flex-wrap"><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/hash-table/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Hash Table</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x155</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/math/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Math</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x91</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/greedy/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Greedy</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x63</span></div></div><div class="flex items-center justify-center text-xs text-label-3 dark:text-dark-label-3"><span class="cursor-pointer">Show more</span></div></div><div class="pb-1"><div class="flex items-center text-xs"><span class="mr-1.5 flex"><span class="inline-block h-1 w-1 rounded-full bg-green-s dark:bg-dark-green-s"></span></span><span class="font-medium">Fundamental</span></div><div class="mt-3 flex flex-wrap"><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/array/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Array</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x391</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/string/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">String</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x174</span></div><div class="mb-3 mr-4 inline-block text-xs"><a href="/tag/sorting/"><span class="inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full bg-fill-3 dark:bg-dark-fill-3 cursor-pointer transition-all hover:bg-fill-2 dark:hover:bg-dark-fill-2 text-label-2 dark:text-dark-label-2">Sorting</span></a><span class="pl-1 text-xs text-label-3 dark:text-dark-label-3">x89</span></div></div><div class="flex items-center justify-center text-xs text-label-3 dark:text-dark-label-3 pb-3"><span class="cursor-pointer">Show more</span></div></div></div>`;

            tar.insertAdjacentElement("afterend",newDiv.firstElementChild);
            }

            let el=document.getElementsByClassName('text-label-2 dark:text-dark-label-2 flex w-full items-center overflow-y-hidden')[0];

            if(el && el.nextElementSibling){

            el.nextElementSibling.remove();

            el.insertAdjacentHTML("afterend",`<div class="flex flex-col"><a class="flex h-[56px] items-center rounded px-4 bg-fill-4 dark:bg-dark-fill-4" target="_blank" href="/submissions/detail/2000803747/"><div data-title="Maximum Subarray" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Maximum Subarray</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">16 hours ago</span></div></a><a class="flex h-[56px] items-center rounded px-4" target="_blank" href="/submissions/detail/2000467735/"><div data-title="Separate the Digits in an Array" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Separate the Digits in an Array</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">a day ago</span></div></a><a class="flex h-[56px] items-center rounded px-4 bg-fill-4 dark:bg-dark-fill-4" target="_blank" href="/submissions/detail/1999799022/"><div data-title="Concatenate Array With Reverse" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Concatenate Array With Reverse</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">2 days ago</span></div></a><a class="flex h-[56px] items-center rounded px-4" target="_blank" href="/submissions/detail/1999599991/"><div data-title="Rotate List" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Rotate List</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">2 days ago</span></div></a><a class="flex h-[56px] items-center rounded px-4 bg-fill-4 dark:bg-dark-fill-4" target="_blank" href="/submissions/detail/1999599620/"><div data-title="Simplify Path" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Simplify Path</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">2 days ago</span></div></a><a class="flex h-[56px] items-center rounded px-4" target="_blank" href="/submissions/detail/1999599273/"><div data-title="Set Matrix Zeroes" class="flex flex-1 justify-between"><span class="text-label-1 dark:text-dark-label-1 line-clamp-1 font-medium">Set Matrix Zeroes</span><span class="text-label-3 dark:text-dark-label-3 hidden whitespace-nowrap lc-md:inline">2 days ago</span></div></a></div>`);
            }


            //}

            document.getElementsByClassName('flex cursor-pointer items-center gap-1')[0].children[0].innerText=`${Math.floor(Math.random()*11)}`;
            document.getElementsByClassName('flex cursor-pointer items-center gap-1')[1].children[0].innerText=`${Math.floor(Math.random()*71)+30}`;
            }
                ''')

            elements = page.locator(
                '[class="bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg my-4 hidden h-[200px] w-full p-4 lc-lg:mt-0 lc-xl:flex"]'
            )

            # btw common parent class => document.getElementsByClassName('relative w-full lc-lg:max-w-[calc(100%_-_316px)]')
            if await elements.count() == 0:
                print("don't exist")
                yield json.dumps({
                    "status": "looks like user dont have enough things LOL"
                }) + "\n"
                # populate it
                html_div = await get_top_chart_n_stuff_const()
                # push the above div sting as children of this => document.getElementsByClassName('relative w-full lc-lg:max-w-[calc(100%_-_316px)]')
                # ti to be first child of this div
                await page.evaluate(
                    """({html}) => {
                        const parent = document.getElementsByClassName(
                            'relative w-full lc-lg:max-w-[calc(100%_-_316px)]'
                        )[0];

                        parent.insertAdjacentHTML('afterbegin', html);
                    }""",
                    {"html": html_div}
                )


            else:
                # print("exist")
                print('lookslike user already is good')
                print('still procedding with few new twerks')
                yield json.dumps({
                    "status": "lookslike user already is good"
                }) + "\n"

                yield json.dumps({
                    "status": "still procedding with few new twerks"
                }) + "\n"
                await elements.first.evaluate("element => element.remove()")
                html_div = await get_top_chart_n_stuff_const()

                await page.evaluate(
                    """({html}) => {
                        const parent = document.getElementsByClassName(
                            'relative w-full lc-lg:max-w-[calc(100%_-_316px)]'
                        )[0];

                        parent.insertAdjacentHTML('afterbegin', html);
                    }""",
                    {"html": html_div}
                )

            """ list of all the elemnts 
            document.getElementsByClassName('hidden h-auto w-full flex-1 items-center justify-center lc-md:flex')[0].children[0].childNodes

            let starting_month = document.getElementsByClassName('hidden h-auto w-full flex-1 items-center justify-center lc-md:flex')[0].children[0].childNodes[13].textContent.toLowerCase()
            """

            starting_month = await page.evaluate("""
            () => {
                return document.getElementsByClassName(
                    'hidden h-auto w-full flex-1 items-center justify-center lc-md:flex'
                )[0].children[0].childNodes[13].textContent.toLowerCase();
            }
            """)

            # print(starting_month)
            month_number = datetime.strptime(starting_month, "%b").month
            # print(month_number)

            # print(create_all_labels_list_to_append(month_number, starting_month.title()))
            list_of_array = await create_all_labels_list_to_append(month_number,
                                                                   starting_month.title())  # ['<text x="8.64" y="97.14" font-size="14px" fill="#AFB4BD" class="font-xs">Aug</text>', '<image xlink:href="/static/images/badges/dcc-2025-9.png" x="64.91" y="82.64" width="22" height="22"></image>', '<image xlink:href="/static/images/badges/dcc-2025-10.png" x="126.94" y="82.64" width="22" height="22"></image>', '<image xlink:href="/static/images/badges/dcc-2025-11.png" x="194.73000000000002" y="82.64" width="22" height="22"></image>', '<image xlink:href="/static/images/badges/dcc-2025-12.png" x="262.52000000000001" y="82.64" width="22" height="22"></image>', '<image xlink:href="/static/images/badges/dcc-2026-1.png" x="324.55" y="82.64" width="22" height="22"></image>', '<image xlink:href="/static/images/badges/dcc-2026-2.png" x="380.81999999999994" y="82.64" width="22" height="22"></image>']
            await page.evaluate(
                """
                (list_of_array) => {
                    const parent = document.getElementsByClassName('hidden h-auto w-full flex-1 items-center justify-center lc-md:flex')[0].children[0];
                    while (parent.children.length > 13) {
                        parent.removeChild(parent.children[13]);
                    }

                    for (const i_html of list_of_array) {
                        parent.insertAdjacentHTML('beforeend' , i_html);
                    }
                }""", list_of_array
            )

            """
            target=document.getElementsByClassName('bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg flex h-auto flex-col space-y-4 p-4 pb-0 lc-md:pb-4')[0].parentNode.nextElementSibling
            """
            html = await get_bottom_table_n_stuff()

            await page.evaluate("""
            (html) => {
                const target = document.getElementsByClassName(
                    'bg-layer-1 dark:bg-dark-layer-1 shadow-down-01 dark:shadow-dark-down-01 rounded-lg flex h-auto flex-col space-y-4 p-4 pb-0 lc-md:pb-4'
                )[0].parentNode.nextElementSibling;

                target.innerHTML = html;
            }
            """, html)
            yield json.dumps({
                "status": "setting up the recent acitivities"
            }) + "\n"
            if change_:
                name = await  r()

                await page.evaluate("""
                (name)=>{
                    document.getElementsByClassName('text-label-3 dark:text-dark-label-3 text-xs')[0].parentNode.previousElementSibling.children[0].innerText=name;
                    document.getElementsByClassName('text-label-3 dark:text-dark-label-3 text-xs')[0].innerText=name;
                }
                """, name)

            yield json.dumps({
                "status": "all set applying just few final tochups"
            }) + "\n"
            await page.wait_for_timeout(8000)
            screenshot_bytes = await page.screenshot()

            await browser.close()

            yield json.dumps({
                "status": "complete",
                "number": change_,
                "screenshot": base64.b64encode(
                    screenshot_bytes
                ).decode()
            }) + "\n"
    return StreamingResponse(
        main_(),
        media_type="application/x-ndjson"
    )

@app.get("/health")
def health():
    return {"status": "healthy"}
# uvicorn main:app --reload
