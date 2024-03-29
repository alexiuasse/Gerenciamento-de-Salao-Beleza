#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 06/09/2020 09:56.

class Bar:

    def __init__(self, series, categories=[], height=250, chart_type='bar', title="", subtitle=""):
        self.title = title
        self.subtitle = subtitle
        self.height = height
        self.series = series
        self.chart_type = chart_type
        # self.colors = colors
        self.categories = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        # [{
        #     data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
        # }]

    def get_options(self):
        return {
            'series': self.series,
            'chart': {
                'height': self.height,
                'type': self.chart_type,
            },
            'plotOptions': {
                'bar': {
                    'barHeight': '100%',
                    'distributed': 1,
                    'horizontal': 1,
                    'dataLabels': {
                        'position': 'bottom'
                    },
                }
            },
            # 'colors': self.colors,
            'dataLabels': {
                'enabled': 0,
                # 'textAnchor': 'start',
                # 'style': {
                #     'colors': ['#fff']
                # },
            },
            'stroke': {
                'width': 1,
                'colors': ['#fff']
            },
            'xaxis': {
                'categories': self.categories
            },
            'yaxis': {
                'labels': {
                    'show': 1
                }
            },
            'title': {
                'text': self.title,
                'align': 'center',
                'floating': 1
            },
            'subtitle': {
                'text': self.subtitle,
                'align': 'center',
            },
            'tooltip': {
                'theme': 'dark',
                'x': {
                    'show': 0
                },
            },
        }
