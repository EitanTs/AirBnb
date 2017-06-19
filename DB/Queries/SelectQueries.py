BED_AVG_RANK = """select a.BedId, r.ParamKey, avg(r.ParamValue) as avarage
from Availabilities as a
left join Beds as b
on a.BedId = b.BedId
join RoomRating as r
on r.RoomId = b.RoomId
where 1=1
and date between '{check_in}' and '{check_in}'
and RenterId = ''
group by r.ParamKey, b.BedId"""