function toggle() {
	numbers.activate()
}

function menuListHandler() {
	alert('value = '+this.list.value)
}

numbers = new MenuList(0,162,165,21)
numbers.overOpen = true  // mouse over opens the next menulist

numbers.list.setImage('images/0.gif','images/1.gif',12,18)

// when you click on a list item it will redirect based on the VALUES sent to the list's
numbers.onSelect = MenuListRedirect

numbers.list.add('javascript:parent.location.href = "index.html"','&nbsp;&nbsp;<b>Home</b>')
numbers.list.add(1,'&nbsp;&nbsp;<b>Support</b>')
numbers.list.add(2,'&nbsp;&nbsp;<b>Contact Us</b>')
numbers.list.add(3,'&nbsp;&nbsp;<b>Products</b>')
numbers.list.add(4,'&nbsp;&nbsp;<b>Services</b>')
numbers.list.add(5,'&nbsp;&nbsp;<b>About Us</b>')
numbers.list.add(6,'&nbsp;&nbsp;<b>Industry Links</b>')
	 
numbers1 = new MenuList(numbers,1)
numbers1.list.add('supp_temp.cgi?sub_link=cs','Customer Service')
numbers1.list.add('supp_temp.cgi?sub_link=ts','Technical Support')  

numbers2 = new MenuList(numbers,2)
numbers2.list.add('cont_temp.cgi?sub_link=access_request','Store Access Request')
numbers2.list.add('cont_temp.cgi?sub_link=credit','Credit Application')
numbers2.list.add('cont_temp.cgi?sub_link=gencomments','General Comments')
numbers2.list.add('cont_temp.cgi?sub_link=sitecomments','Site Comments')


numbers3 = new MenuList(numbers,3)
numbers3.list.add('#','Desktop PCs')
numbers3.list.add('#','Workstations')
numbers3.list.add('#','PIII Servers')
numbers3.list.add('#','Xeon&#153; Servers')

    numbers3_0 = new MenuList(numbers3,0)
    numbers3_0.list.add('prod_temp.cgi?sub_link=thresher&title=thresher','Thresher Series&#153;')
	
    numbers3_0 = new MenuList(numbers3,1)
    numbers3_0.list.add('prod_temp.cgi?sub_link=mako&title=mako','Mako Series&#153;')

    numbers3_0 = new MenuList(numbers3,2)
    numbers3_0.list.add('prod_temp.cgi?sub_link=tiger&title=tiger','Tiger Series&#153;')

    numbers3_0 = new MenuList(numbers3,3)
    numbers3_0.list.add('prod_temp.cgi?sub_link=gw&title=gw','Great White Series&#153;')

/*hidden
numbers3.list.add('http://www.flashecom.com/coastlinemicro/dept.asp?dept_id=18','CD-ROM / DVD')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/gdept.asp?dept_id=04','Hard Drives')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/gdept.asp?dept_id=08','Memory')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/dept.asp?dept_id=23','Monitors')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/gdept.asp?dept_id=03','Motherboards')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/dept.asp?dept_id=21','NIC Cards')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/dept.asp?dept_id=11','Power Supply')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/gdept.asp?dept_id=01','Processors')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/dept.asp?dept_id=16','Tape Drives')
numbers3.list.add('http://www.flashecom.com/coastlinemicro/gdept.asp?dept_id=06','Video Adapters')
*/

  /*hidden

    numbers3_0_0 = new MenuList(numbers3_0,0)
    numbers3_0_0.list.add('#','Pentium PIII 700')
    numbers3_0_0.list.add('#','Celeron PII 550')
    numbers3_0_0.list.add('#','Pentium PIII 733')

	    numbers3_0_0_0 = new MenuList(numbers3_0_0,0)
	    numbers3_0_0_0.list.add('#','13G, 64M, V')
    	numbers3_0_0_0.list.add('#','13G, 64M, A/V')

	    numbers3_0_0_0 = new MenuList(numbers3_0_0,1)
	    numbers3_0_0_0.list.add('#','13G, 64M, V')
    	numbers3_0_0_0.list.add('#','13G, 64M, A/V')
    	numbers3_0_0_0.list.add('#','13G, 64M, A/V/N')

	    numbers3_0_0_0 = new MenuList(numbers3_0_0,2)
	    numbers3_0_0_0.list.add('#','20G, 128M, V')
    	numbers3_0_0_0.list.add('#','20G, 128M, A/V/N')
    	numbers3_0_0_0.list.add('#','20G, 128M, Best A/V')
  */
  
numbers4 = new MenuList(numbers,4)
numbers4.list.add('serv_temp.cgi?sub_link=config','Configuration/Assembly')
numbers4.list.add('serv_temp.cgi?sub_link=inter_intra','Internet/Intranet')
numbers4.list.add('serv_temp.cgi?sub_link=networking','Networking')
numbers4.list.add('serv_temp.cgi?sub_link=requirement','Requirement Analysis')
numbers4.list.add('serv_temp.cgi?sub_link=shipping','Shipping')
numbers4.list.add('serv_temp.cgi?sub_link=testing','Testing')


  
numbers5 = new MenuList(numbers,5)
numbers5.list.add('about_temp.cgi?sub_link=location','Company Location')
numbers5.list.add('about_temp.cgi?sub_link=heritage','Heritage')
numbers5.list.add('press.cgi','Press Releases / News')
numbers5.list.add('about_temp.cgi?sub_link=auth','Product Authorizations')


numbers6 = new MenuList(numbers,6)
numbers6.list.add('javascript:window.open("go.cgi?new_url=http://www.channelweb.com/");location.reload()','ChannelWeb.com')
numbers6.list.add('javascript:window.open("go.cgi?new_url=http://www.cmp.com/");location.reload()','CMP.com')
numbers6.list.add('javascript:window.open("go.cgi?new_url=http://www.crn.com/");location.reload()','CRN.com')
numbers6.list.add('javascript:window.open("go.cgi?new_url=http://www.networkvar.com/");location.reload()','NetworkVAR.com')

numbers.build()

writeCSS(
numbers.css
)