class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        day,month,year = date.split(' ')
        day = day[:-2]
        
        for i in range(0,10):
            if int(day) == i:
                day = "0"+day
        
        str1 = year+"-"+months[month]+"-"+day

        return str1


       


        