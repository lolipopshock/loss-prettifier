class LossPrettifier(object):
    
    STYLE = {
        'green' : '\033[32m',
        'red'   : '\033[91m', 
        'bold'  : '\033[1m', 
    }
    STYLE_END = '\033[0m'
    
    def __init__(self, show_percentage=False):
        
        self.show_percentage = show_percentage
        self.color_up = 'green'
        self.color_down = 'red'
        self.loss_terms = {}
    
    def __call__(self, epoch=None, **kwargs):
        
        if epoch is not None:
            print_string = f'Epoch {epoch: 5d} '
        else:
            print_string = ''

        for key, value in kwargs.items():
            
            pre_value = self.loss_terms.get(key, value)
            
            if value > pre_value:
                indicator  = '▲'
                show_color = self.STYLE[self.color_up]
            elif value == pre_value:
                indicator  = ''
                show_color = ''
            else:
                indicator  = '▼'
                show_color = self.STYLE[self.color_down]
            
            if self.show_percentage:
                show_value = 0 if pre_value == 0 \
                             else (value - pre_value) / float(pre_value)
                key_string = f'| {key}: {show_color}{value:3.2f}({show_value:+3.2%}) {indicator}'
            else: 
                key_string = f'| {key}: {show_color}{value:.4f} {indicator}'
            
            # Trim some long outputs
            key_string_part = key_string[:32]
            print_string += key_string_part+f'{self.STYLE_END}\t'
            
            self.loss_terms[key] = value
            
        print(print_string)
