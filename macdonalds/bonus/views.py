from django.shortcuts import render_to_response,get_object_or_404,HttpResponse


# bonus gifts list
def bonusGifts(request):
    return render_to_response('bonus/gifts.html',locals())
    
    #兑换麦当劳
def redeem(request):
    return render_to_response('bonus/redeem.html',locals())
    
    # 幸运抽奖
def luckyExchange(request):
    return render_to_response('bonus/lucky.html',locals())
    
    # 账本收入
def bonusIncoming(request):
    return render_to_response('bonus/incoming.html',locals())
    
    # 账本支出
def bonusPaid(request):
    return render_to_response('bonus/paid.html',locals())
    
    # 排行榜
def boards(request):
    return render_to_response('bonus/board.html',locals())