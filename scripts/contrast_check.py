#!/usr/bin/env python3
from math import pow

COLORS = {
    'ink': '#1B1B1F',
    'muted': '#4B5563',
    'gray-500': '#444444',
    'gray-600': '#4B4B50',
    'brand': '#9605DF',
    'brand-dark': '#7E04B9',
    'white': '#FFFFFF',
    'bg-muted': '#F5F5F5',
    'bg-light': '#FAFAFA',
}

PAIRS = [
    ('ink', 'white'),
    ('ink', 'bg-muted'),
    ('ink', 'bg-light'),
    ('muted', 'white'),
    ('muted', 'bg-muted'),
    ('muted', 'bg-light'),
    ('gray-500', 'white'),
    ('gray-600', 'white'),
    ('brand', 'white'),
    ('white', 'brand'),
    ('white', 'brand-dark'),
]

def luminance(rgb):
    srgb=[]
    for c in rgb:
        c/=255
        srgb.append(c/12.92 if c<=0.03928 else pow((c+0.055)/1.055,2.4))
    r,g,b=srgb
    return 0.2126*r+0.7152*g+0.0722*b

def contrast_ratio(hex1,hex2):
    def hex_to_rgb(h):
        h=h.lstrip('#')
        if len(h)==3:
            h=''.join(c*2 for c in h)
        return tuple(int(h[i:i+2],16) for i in (0,2,4))
    lum1=luminance(hex_to_rgb(hex1))
    lum2=luminance(hex_to_rgb(hex2))
    lighter=max(lum1,lum2)
    darker=min(lum1,lum2)
    return (lighter+0.05)/(darker+0.05)

if __name__ == '__main__':
    for fg, bg in PAIRS:
        ratio=contrast_ratio(COLORS[fg], COLORS[bg])
        print(f"{fg} on {bg}: {ratio:.2f}")
