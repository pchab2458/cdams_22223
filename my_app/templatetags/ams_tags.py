from django import template
from django.utils.safestring import mark_safe
import markdown
from django.shortcuts import get_object_or_404

# from ams.models import Billing
# from ams.models import TenantProfile

from my_app.models import Billing, Room_type, Room
from my_app.models import TenantProfile

register = template.Library()


#
# @register.simple_tag
# def total_posts():
#     return Post.published.count()
#
#
# @register.simple_tag
# def total_posts_pluralize():
#     s = ''
#     if Post.objects.count() > 1:
#         s = 's'
#     return s
#
#
# @register.inclusion_tag('blog/post/latest_posts.html')
# def show_latest_posts(count=5):
#     # latest_posts = Post.published.order_by('-publish')[:count]
#     latest_posts = Post.published.order_by('-publish')[:count]
#     return {'latest_posts': latest_posts}
#
#
# @register.simple_tag
# def get_most_commented_posts(count=5):
#     return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.inclusion_tag('my_app/display_tenant_data.html')
def display_tenant_data(rmno):
    tenant_data = get_object_or_404(TenantProfile, room_no__room_no=rmno)  # str vs str !!!!

    return {'tenant_data': tenant_data}


@register.filter
# @register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# @register.inclusion_tag('blog/post/latest_posts.html',name='show_latest_post_pb_test')
# def show_latest_posts_pb(count=5):
#     latest_posts = Post.published.order_by('-publish')[:count]
#     content = {'latest_posts':latest_posts}
#
#     return content


@register.inclusion_tag('my_app/payment_tag.html')
def display_tenant_bill_data(rmno):
    tenant_bill = get_object_or_404(Billing, room_no=rmno, status='open')

    rm_c_ac_c_plus_adj = tenant_bill.room_cost + tenant_bill.room_acc_cost + tenant_bill.adjust

    bill_misc = tenant_bill.late_fee + tenant_bill.maint_cost

    return {'tenant_bill': tenant_bill, 'rm_c_ac_c_plus_adj': rm_c_ac_c_plus_adj, 'bill_misc': bill_misc}


@register.inclusion_tag('my_app/payment_individual_tag.html')
def display_individual_tenant_bill_data(rmno):
    tenant_bill = get_object_or_404(Billing, room_no=rmno, status='open')

    room_cost_acc = tenant_bill.room_cost + tenant_bill.room_acc_cost + tenant_bill.adjust

    bill_misc = tenant_bill.late_fee + tenant_bill.maint_cost

    return {'tenant_bill': tenant_bill, 'room_cost_acc': room_cost_acc, 'bill_misc': bill_misc}


@register.simple_tag
def room_acc_cost(rmno):
    tenant_pf = get_object_or_404(TenantProfile, room_no__room_no=rmno)
    extra = tenant_pf.extra.all()

    exd = {}
    exd.setdefault('Electricity CPU', 0)
    exd.setdefault('Water CPU', 0)
    exd.setdefault('Garbage', 0)
    exd.setdefault('Bed&Mattress', 0)
    exd.setdefault('Clothing Cupboard', 0)
    exd.setdefault('Dressing Table', 0)
    exd.setdefault('TV Table', 0)
    exd.setdefault('Wifi', 0)
    exd.setdefault('Fridge', 0)
    exd.setdefault('Air-Conditioner', 0)
    exd.setdefault('Parking', 0)

    for e in extra:
        exd.update({e.description: e.cpu})

    room_acc_cost = exd['Bed&Mattress'] + exd['Clothing Cupboard'] + exd['Dressing Table'] + exd['TV Table'] + exd['Fridge'] + exd['Air-Conditioner']

    # return '{0:3,.0f}'.format(room_acc_cost)
    return '{:,.0f}'.format(room_acc_cost)


@register.simple_tag
def room_other_cost(rmno):
    tenant_pf = get_object_or_404(TenantProfile, room_no__room_no=rmno)
    extra = tenant_pf.extra.all()

    exd = {}
    exd.setdefault('Electricity CPU', 0)
    exd.setdefault('Water CPU', 0)
    exd.setdefault('Garbage', 0)
    exd.setdefault('Bed&Mattress', 0)
    exd.setdefault('Clothing Cupboard', 0)
    exd.setdefault('Dressing Table', 0)
    exd.setdefault('TV Table', 0)
    exd.setdefault('Wifi', 0)
    exd.setdefault('Fridge', 0)
    exd.setdefault('Air-Conditioner', 0)
    exd.setdefault('Parking', 0)

    for e in extra:
        exd.update({e.description: e.cpu})

    oth_ser_cost = exd['Garbage'] + exd['Parking'] + exd['Wifi']

    # return '{0:>3,.0f}'.format(oth_ser_cost)
    return '{:,.0f}'.format(oth_ser_cost)


@register.simple_tag
def room_cost_plus_acc_cost_with_adj(tn_bill):
    rm_c_acc_c = tn_bill.room_cost + tn_bill.room_acc_cost + tn_bill.adjust

    return '{0:,.0f}'.format(rm_c_acc_c)


@register.simple_tag
def late_fee_plus_ma(tn_bill):
    lf_ma = tn_bill.late_fee + tn_bill.maint_cost

    return '{0:,.0f}'.format(lf_ma)


@register.simple_tag
def late_fee_plus_ma_ab(tn_bill_a, tn_bill_b):
    lf_ma_a = tn_bill_a.late_fee + tn_bill_a.maint_cost
    lf_ma_b = tn_bill_b.late_fee + tn_bill_b.maint_cost
    total_lf_ma = lf_ma_a + lf_ma_b

    return '{0:,.0f}'.format(total_lf_ma)


@register.simple_tag
def room_cost(rmn):
    rmn_rmc_dict = {}
    all_room = Room.objects.all()
    for rm in all_room:
        rmn_rmc_dict.update({rm.room_no: rm.room_type.rate})

    rm_cost = rmn_rmc_dict[rmn]

    # return '{0:,.0f}'.format(rm_cost)
    return '{:,.0f}'.format(rm_cost)
