months_={'sep':'https://leetcode.com/static/images/badges/dcc-2025-9.png','oct':'https://leetcode.com/static/images/badges/dcc-2025-10.png','nov':'https://leetcode.com/static/images/badges/dcc-2025-11.png','dec':'https://leetcode.com/static/images/badges/dcc-2025-12.png',
         'jan':'https://leetcode.com/static/images/badges/dcc-2026-1.png','feb':'https://leetcode.com/static/images/badges/dcc-2026-2.png',
         'mar':'https://leetcode.com/static/images/badges/dcc-2026-3.png','apr':'https://leetcode.com/static/images/badges/dcc-2026-4.png',
         'may':'https://leetcode.com/static/images/badges/dcc-2026-5.png','jun':'https://leetcode.com/static/images/badges/dcc-2026-6.png',
         'jul':'https://leetcode.com/static/images/badges/dcc-2026-7.png','aug':'https://leetcode.com/static/images/badges/dcc-2026-8.png',
         }
change_=1
pfp_url='https://leetcode.com/u/d1zpNU7oGC/'
from playwright.async_api import async_playwright
import asyncio
from datetime import datetime


async def main(pfp_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ]
        )

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


        await context.add_init_script("Object.defineProperty(navigator,'webdriver',{get: ()=>undefined})")

        page=await context.new_page()

        print(f'page khul gaya at {datetime.now().strftime("%H:%M:%S")}')

        await page.goto(pfp_url, wait_until="networkidle", timeout=30000)


        await page.wait_for_timeout(3000)

        print("Title:", await page.title())
        print("URL:", page.url)
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
        let _a1=Math.floor(Math.random()*(900-300+1))+300;
        let _a2=Math.floor(Math.floor(Math.random()*(900-300+1))+100);
        _a2/=7;
        _a2=Math.floor(_a2);
        document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0].parentNode.childNodes[0].children[2].innerText=`${_a1}`;
        document.getElementsByClassName('flex items-center space-x-2 text-[14px]')[0].parentNode.childNodes[1].children[1].innerText=`${_a2}`;


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


        let _b1=Math.floor(Math.random()*10)+1;
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

        await page.screenshot(path="pfp.png")

        await browser.close()


asyncio.run(main(pfp_url))
