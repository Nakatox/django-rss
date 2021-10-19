window.addEventListener('DOMContentLoaded', () => {
    const categoryNew = document.querySelector('.display_mode_container_category_text.new')
    const categoryHot = document.querySelector('.display_mode_container_category_text.hot')
    const mode1 = document.querySelector('.display_mode_container_mode.mode1')
    const mode2 = document.querySelector('.display_mode_container_mode.mode2')
    
    const card = document.querySelector('.article_card')
    const cardStat = document.querySelector('.article_card_stat')
    const cardRank = document.querySelector('.article_card_rank')

    const activeSwitcher = (toggle1, toggle2) => {
        toggle1.addEventListener('click', () => {
            if (toggle1.classList.contains('active') === false) {
                toggle1.classList.add('active')
                toggle2.classList.remove('active')
            }
        })
    }

    activeSwitcher(categoryNew, categoryHot)
    activeSwitcher(categoryHot, categoryNew)
    activeSwitcher(mode1, mode2)
    activeSwitcher(mode2, mode1)

    mode2.addEventListener('click', () => {
        card.style.width = "30%"
        card.style.maxWidth = "280px"
        card.style.flexDirection = "column"
        card.style.height = "350px"
        card.style.padding = "20px 15px"
        card.style.alignItems = "flex-start"

        cardStat.style.width = "100%"
        cardStat.style.justifyContent = "space-between"

        cardRank.style.borderRight = "none"
    })  

    mode1.addEventListener('click', () => {
        card.style.width = "100%"
        card.style.maxWidth = "initial"
        card.style.flexDirection = "row"
        card.style.height = "initial"
        card.style.padding = "0 25px"
        card.style.alignItems = "center"

        cardStat.style.width = "initial"
        cardStat.style.justifyContent = "center"

        cardRank.style.borderRight = "solid 1px #fff"
    })
})