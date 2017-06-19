BED_AVG_RANK = """select a.BedId, r.ParamKey, avg(r.ParamValue) as average, date
from Availabilities as a
left join Beds as b
on a.BedId = b.BedId
join RoomRating as r
on r.RoomId = b.RoomId
where 1=1
and date between '{check_in}' and '{check_out}'
and RenterId = ''
group by date, r.ParamKey, b.BedId"""


USER_PREFRENCES = """ select ParamKey, ParamValue
from Preferences
where 1=1
and UserId = '{user_id}'"""