$(function(){
    var $items = $('.grid').find('.grid-item');
    var $grid = $('.grid').isotope({
      itemSelector: '.grid-item',
      percentPosition: true,
      masonry: {
        columnWidth: '.grid-sizer'
      },
      getSortData : {
        name : function ( $items ) {
          return $items.outerText;
        }
      }
    });

    // layout Isotope after each image loads
    $grid.imagesLoaded().progress( function() {
      $grid.isotope('layout');
    });

    // bind sort button click
    $('.button').on('click', function() {
        var id = $(this).attr('id');
        switch(id) {
            case 'random':
               $grid.isotope({ sortBy: 'random' });
                break;
            case 'original':
                $grid.isotope({ sortBy: 'original-order' });
                break;
            case 'ascending':
               $grid.isotope({ sortBy: 'name' });
                break;
            case 'author1':
               $grid.isotope({ filter: '.Amanda' });
                break;
            case 'author2':
               $grid.isotope({ filter: '.Don' });
                break;
            case 'all':
               $grid.isotope({ filter: '*' });
                break;
            default:
            break;
        }
    });
});
