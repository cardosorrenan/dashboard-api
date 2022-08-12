module WelcomesHelper
  def welcome_title_label
    if current_user.admin?
      content_tag :span, 'Acesso do Administrador', class: 'label label-danger'
    else
      content_tag :span, 'Acesso do Cliente', class: 'label label-info'
    end
  end
end
